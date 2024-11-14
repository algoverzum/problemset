#include <algorithm>
#include <iostream>
#include <utility>
#include <vector>
#include <random>

const int MAXB = 20; //max value: 2^MAXB

bool edges[MAXB][MAXB]; //aviable edges
bool possible_values[1<<MAXB];
std::vector<int> values;

void generate_edges_dense(std::mt19937& rnd, int B, int prob = 1){
    std::uniform_int_distribution<> dist(0, prob);
    for(int i = 0; i < B; i++){
        for(int j = i + 1; j < B; j++){
            edges[i][j] = edges[j][i] = dist(rnd);
        }
    }
}

void generate_tree_like(std::mt19937 &rnd, int B, int extra = 0){
    std::vector<int> ord(B);
    std::iota(ord.begin(), ord.end(), 0);
    for(int i = 1; i < B; i++){
        int p = rnd() % i;
        edges[ord[p]][ord[i]] = edges[ord[i]][ord[p]] = true;
    }

    std::uniform_int_distribution<> dist(0, B-1);
    for(int i = 0; i < extra; i++){
        int x = dist(rnd);
        int y = dist(rnd);
        while(x == y) y = dist(rnd);
        edges[x][y] = edges[y][x] = true;
    }
}

void generate_disjoint(std::mt19937 &rnd, int B){
    int split = rnd() % (B - 3) + 1;
    for(int i = 0; i < B; i++){
        for(int j = i+1; j < B; j++){
            if((i <= split) == (j <= split)){
                edges[i][j] = edges[j][i] = true;
            }
        }
    }
}

void calc_possible_values(std::mt19937 &rnd, int B){
    for(int x = 0; x < (1<<B); x++){
        bool ok = true;
        for(int i = 0; i < B; i++){
            for(int j = 0; j < i; j++){
                if(((x>>i)&1) && ((x>>j)&1) && !edges[i][j]){
                    ok = false;
                }
            }
        }
        if(ok) possible_values[x] = true;
    }

    for(int i = 0; i < (1<<B); i++){
        if(possible_values[i]){
            values.push_back(i);
        }
    }
    std::shuffle(values.begin(), values.end(), rnd);
}

std::vector<int> get_vals_random(std::mt19937 &rnd, const std::vector<int>& pool, int N){
    std::vector<int> res(N);
    std::uniform_int_distribution<> dist(0, (int)pool.size() - 1);

    for(int &x : res) x = pool[dist(rnd)];
    return res;
}

std::vector<int> get_vals_cyclic(const std::vector<int>& pool, int N){
    std::vector<int> res(N);
    for(int i = 0; i < N; i++) res[i] = pool[i % (int)pool.size()];
    return res;
}

std::vector<std::pair<int, int>> get_random_queries(std::mt19937 &rnd, int N, int Q){
    std::vector<std::pair<int, int>> res(Q);
    std::uniform_int_distribution<> dist(1, N);

    for(auto &[x, y] : res){
        x = dist(rnd);
        do{
            y = dist(rnd);
        } while(x == y);
    }
    return res;
}

int main(int argc, char* argv[]){
    if(argc != 6){
        return 1;
    }

    const int N = atoi(argv[1]);
    const int Q = atoi(argv[2]);
    const int B = atoi(argv[3]);
    const int T = atoi(argv[4]);
    const int SEED = atoi(argv[5]);

    std::mt19937 rnd(SEED);

    std::vector<int> vertex_vals;
    std::vector<std::pair<int, int>> queries;
    switch (T)
    {
    case 0:
        generate_edges_dense(rnd, B);
        calc_possible_values(rnd, B);
        vertex_vals = rnd()%2 ? get_vals_random(rnd, values, N) : get_vals_cyclic(values, N);
        queries = get_random_queries(rnd, N, Q);
        break;
    case 1:
        generate_tree_like(rnd, B, rnd()%std::min((B + 1) / 2, 5));
        calc_possible_values(rnd, B);
        vertex_vals = rnd()%2 ? get_vals_random(rnd, values, N) : get_vals_cyclic(values, N);
        queries = get_random_queries(rnd, N, Q);
        break;
    case 2:
        generate_disjoint(rnd, B);
        calc_possible_values(rnd, B);
        vertex_vals = rnd()%2 ? get_vals_random(rnd, values, N) : get_vals_cyclic(values, N);
        queries = get_random_queries(rnd, N, Q);
        break;
    case 3:
        generate_edges_dense(rnd, B, 9);
        calc_possible_values(rnd, B);
        vertex_vals = rnd()%2 ? get_vals_random(rnd, values, N) : get_vals_cyclic(values, N);
        queries = get_random_queries(rnd, N, Q);
    }

    std::shuffle(vertex_vals.begin(), vertex_vals.end(), rnd);
    std::shuffle(queries.begin(), queries.end(), rnd);

    std::cout << N << ' ' << Q << '\n';
    for(int i = 0; i < N; i++){
        std::cout << vertex_vals[i] << " \n"[i == N-1];   
    }
    for(auto [x, y] : queries){
        std::cout << x << ' ' << y << '\n';
    }

    return 0;
}