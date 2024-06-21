import pandas as pd
df = pd.read_csv('pe8_data.csv')

# 問題1: 東區哪些球隊的主場勝率低於客場勝率？
def win_pct(record):
    wins, losses = map(int, record.split('-'))
    return wins / (wins + losses)
east_teams = df[df['Conference'] == 'Eastern']
east_teams['Home_Win_Pct'] = east_teams['HOME'].apply(win_pct)
east_teams['Away_Win_Pct'] = east_teams['AWAY'].apply(win_pct)
east_teams_home_away = east_teams[east_teams['Home_Win_Pct'] < east_teams['Away_Win_Pct']]
teams_home_lower_away = east_teams_home_away['Team'].tolist()

print("東區主場勝率低於客場勝率的球隊: ", teams_home_lower_away)

# 問題2: 哪一區的球隊擁有較高的“平均得分減掉失分”？
df['PF_minus_PA'] = df['PF'] - df['PA']
average_pf_minus_pa = df.groupby('Conference')['PF_minus_PA'].mean()
higher_average_pf_minus_pa_conference = average_pf_minus_pa.idxmax()

print("擁有較高“平均得分減掉失分”的區: ", higher_average_pf_minus_pa_conference)

# 問題3: 根據每支球隊和另一區球隊的對戰記錄來對所有球隊排序
sorted_teams_by_pct = df.sort_values(by='PCT', ascending=False)['Team'].tolist()

print("根據對戰另一區球隊的勝率(PCT)排序的球隊: ", sorted_teams_by_pct)