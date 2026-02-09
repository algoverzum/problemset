// @check-accepted: *
#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    int n;
    cin >> n;
    vector<string> names;
    vector<int> scores;
    for (int i = 0; i < n; i++) {
        string name;
        int score;
        cin >> name >> score;
        names.push_back(name);
        scores.push_back(score);
    }
    int fails = 0;
    for (int score : scores) {
        if (score < 50) {
            fails++;
        }
    }
    int max_score = scores[0];
    for (int i = 1; i < n; i++) {
        if (scores[i] > max_score) {
            max_score = scores[i];
        }
    }
    int min_score = scores[0];
    for (int i = 1; i < n; i++) {
        if (scores[i] < min_score) {
            min_score = scores[i];
        }
    }
    int best_index =
        find(scores.begin(), scores.end(), max_score) - scores.begin();
    int worst_index =
        find(scores.begin(), scores.end(), min_score) - scores.begin();
    string best_name = names[best_index];
    string worst_name = names[worst_index];
    vector<int> sorted_scores = scores;
    sort(sorted_scores.begin(), sorted_scores.end());
    vector<string> passed_students;
    for (int i = 0; i < n; i++) {
        if (scores[i] >= 50) {
            passed_students.push_back(names[i]);
        }
    }
    cout << "Megbuktak: " << fails << endl;
    cout << "Legjobb: " << best_name << " (" << max_score << ")" << endl;
    cout << "Legrosszabb: " << worst_name << " (" << min_score << ")" << endl;
    cout << "Rendezett pontok:";
    for (int score : sorted_scores) {
        cout << " " << score;
    }
    cout << endl;
    cout << "Átmentek:";
    if (passed_students.empty()) {
        cout << " -" << endl;
    } else {
        for (const string &name : passed_students) {
            cout << " " << name;
        }
        cout << endl;
    }
    return 0;
}
