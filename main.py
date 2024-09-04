import streamlit as st
import pandas as pd
import plotly.express as px

# タクシーデータ
taxi_data = [
    {'month': '2022年9月', '日本交通': 108.3616, '東京無線': 58.5976, '国際自動車': 47.2001, '帝都自動車交通': 15.2354, '大和自動車交通': 10.0715, '荏原交通': 5.9750, 'グリーンキャブ': 4.6794, '東都タクシー': 4.2906, '私鉄共同無線': 4.1376, '東個協': 12.5460, '日個連都営協': 8.5764},
    {'month': '2022年10月', '日本交通': 115.5650, '東京無線': 62.4587, '国際自動車': 52.3495, '帝都自動車交通': 16.3873, '大和自動車交通': 10.5514, '荏原交通': 6.1920, 'グリーンキャブ': 4.7794, '東都タクシー': 4.2738, '私鉄共同無線': 4.2028, '東個協': 12.7869, '日個連都営協': 8.6383},
    {'month': '2022年11月', '日本交通': 109.9876, '東京無線': 59.3631, '国際自動車': 50.0652, '帝都自動車交通': 15.3937, '大和自動車交通': 9.6476, '荏原交通': 5.7766, 'グリーンキャブ': 4.6741, '東都タクシー': 4.1420, '私鉄共同無線': 3.9561, '東個協': 11.0854, '日個連都営協': 6.3200},
    {'month': '2022年12月', '日本交通': 132.0327, '東京無線': 70.0334, '国際自動車': 58.8862, '帝都自動車交通': 17.9391, '大和自動車交通': 11.9536, '荏原交通': 6.5996, 'グリーンキャブ': 5.1521, '東都タクシー': 4.6894, '私鉄共同無線': 4.5457, '東個協': 13.1689, '日個連都営協': 7.5225},
    {'month': '2023年1月', '日本交通': 111.5881, '東京無線': 56.8834, '国際自動車': 48.7519, '帝都自動車交通': 13.5111, '大和自動車交通': 9.5344, '荏原交通': 5.6586, 'グリーンキャブ': 4.9454, '東都タクシー': 4.4086, '私鉄共同無線': 3.7026, '東個協': 10.7850, '日個連都営協': 5.9075},
    {'month': '2023年2月', '日本交通': 111.7165, '東京無線': 53.0316, '国際自動車': 44.0216, '帝都自動車交通': 12.4019, '大和自動車交通': 8.9839, '荏原交通': 6.0021, 'グリーンキャブ': 4.0513, '東都タクシー': 4.0278, '私鉄共同無線': 3.4984, '東個協': 10.0712, '日個連都営協': 5.4639},
    {'month': '2023年3月', '日本交通': 132.9948, '東京無線': 63.9365, '国際自動車': 57.8788, '帝都自動車交通': 15.4591, '大和自動車交通': 11.2637, '荏原交通': 7.0918, 'グリーンキャブ': 4.8197, '東都タクシー': 4.6200, '私鉄共同無線': 4.0694, '東個協': 11.9372, '日個連都営協': 6.4361},
    {'month': '2023年4月', '日本交通': 123.3547, '東京無線': 59.3468, '国際自動車': 54.4885, '帝都自動車交通': 14.9729, '大和自動車交通': 10.3769, '荏原交通': 7.2407, 'グリーンキャブ': 4.3221, '東都タクシー': 4.2097, '私鉄共同無線': 3.7995, '東個協': 10.6827, '日個連都営協': 5.7584},
    {'month': '2023年5月', '日本交通': 126.5306, '東京無線': 62.1607, '国際自動車': 54.4223, '帝都自動車交通': 15.6292, '大和自動車交通': 10.6058, '荏原交通': 7.3019, 'グリーンキャブ': 4.9063, '東都タクシー': 4.3074, '私鉄共同無線': 3.9084, '東個協': 11.1050, '日個連都営協': 5.8073},
    {'month': '2023年6月', '日本交通': 133.9381, '東京無線': 67.4930, '国際自動車': 62.6311, '帝都自動車交通': 16.6540, '大和自動車交通': 11.5152, '荏原交通': 7.4394, 'グリーンキャブ': 4.9061, '東都タクシー': 4.3753, '私鉄共同無線': 4.1739, '東個協': 12.5243, '日個連都営協': 6.6274},
    {'month': '2023年7月', '日本交通': 149.1895, '東京無線': 75.5356, '国際自動車': 67.3927, '帝都自動車交通': 20.0727, '大和自動車交通': 12.8639, '荏原交通': 8.0858, 'グリーンキャブ': 5.3408, '東都タクシー': 4.9071, '私鉄共同無線': 4.3669, '東個協': 13.3676, '日個連都営協': 6.9349},
    {'month': '2023年8月', '日本交通': 147.3150, '東京無線': 73.3557, '国際自動車': 64.2249, '帝都自動車交通': 20.6340, '大和自動車交通': 12.9024, '荏原交通': 7.9878, 'グリーンキャブ': 5.6037, '東都タクシー': 4.8217, '私鉄共同無線': 4.1927, '東個協': 13.2211, '日個連都営協': 6.9591},
    {'month': '2023年9月', '日本交通': 146.0540, '東京無線': 69.4828, '国際自動車': 64.7162, '帝都自動車交通': 19.7135, '大和自動車交通': 12.9728, '荏原交通': 7.5237, 'グリーンキャブ': 5.4992, '東都タクシー': 4.4185, '私鉄共同無線': 4.0086, '東個協': 12.4046, '日個連都営協': 6.4271},
    {'month': '2023年10月', '日本交通': 141.6900, '東京無線': 64.3908, '国際自動車': 61.9115, '帝都自動車交通': 18.5325, '大和自動車交通': 11.9959, '荏原交通': 6.7910, 'グリーンキャブ': 5.3773, '東都タクシー': 4.2490, '私鉄共同無線': 3.8688, '東個協': 10.8378, '日個連都営協': 5.7392},
    {'month': '2023年11月', '日本交通': 138.7577, '東京無線': 61.5365, '国際自動車': 58.9570, '帝都自動車交通': 18.3923, '大和自動車交通': 11.3516, '荏原交通': 6.6133, 'グリーンキャブ': 5.0494, '東都タクシー': 4.0313, '私鉄共同無線': 3.8006, '東個協': 10.3233, '日個連都営協': 5.5713},
    {'month': '2023年12月', '日本交通': 163.7901, '東京無線': 72.9442, '国際自動車': 68.8706, '帝都自動車交通': 21.8825, '大和自動車交通': 13.3831, '荏原交通': 7.3868, 'グリーンキャブ': 5.4720, '東都タクシー': 4.9384, '私鉄共同無線': 4.5612, '東個協': 12.2989, '日個連都営協': 6.5702},
    {'month': '2024年1月', '日本交通': 143.6288, '東京無線': 59.1370, '国際自動車': 55.1083, '帝都自動車交通': 18.7152, '大和自動車交通': 11.4712, '荏原交通': 6.0925, 'グリーンキャブ': 5.0900, '東都タクシー': 4.0649, '私鉄共同無線': 3.7107, '東個協': 8.9695, '日個連都営協': 6.6014},
    {'month': '2024年2月', '日本交通': 147.4142, '東京無線': 71.7747, '国際自動車': 58.9681, '帝都自動車交通': 20.5645, '大和自動車交通': 12.5125, '荏原交通': 7.9934, 'グリーンキャブ': 5.7362, '東都タクシー': 4.0769, '私鉄共同無線': 3.9018, '東個協': 9.8259, '日個連都営協': 7.3569},
    {'month': '2024年3月', '日本交通': 166.8151, '東京無線': 81.7471, '国際自動車': 70.3799, '帝都自動車交通': 23.2978, '大和自動車交通': 14.0338, '荏原交通': 9.0638, 'グリーンキャブ': 6.6620, '東都タクシー': 4.6689, '私鉄共同無線': 4.5109, '東個協': 11.6773, '日個連都営協': 8.7946},
    {'month': '2024年4月', '日本交通': 155.1393, '東京無線': 74.0784, '国際自動車': 63.5668, '帝都自動車交通': 22.0132, '大和自動車交通': 13.1026, '荏原交通': 8.3566, 'グリーンキャブ': 5.7913, '東都タクシー': 4.0055, '私鉄共同無線': 4.0148, '東個協': 9.7981, '日個連都営協': 7.4612},
    {'month': '2024年5月', '日本交通': 159.1345, '東京無線': 74.9657, '国際自動車': 61.8317, '帝都自動車交通': 22.2832, '大和自動車交通': 13.3492, '荏原交通': 8.8921, 'グリーンキャブ': 5.8109, '東都タクシー': 3.7591, '私鉄共同無線': 3.9899, '東個協': 9.6874, '日個連都営協': 7.5601},
    {'month': '2024年6月', '日本交通': 165.1926, '東京無線': 80.3331, '国際自動車': 65.4062, '帝都自動車交通': 23.5958, '大和自動車交通': 13.6568, '荏原交通': 8.9662, 'グリーンキャブ': 6.7639, '東都タクシー': 0, '私鉄共同無線': 4.1487, '東個協': 10.1832, '日個連都営協': 7.8086},
    {'month': '2024年7月', '日本交通': 188.1398, '東京無線': 98.9619, '国際自動車': 76.0363, '帝都自動車交通': 28.7805, '大和自動車交通': 16.2645, '荏原交通': 10.2809, 'グリーンキャブ': 7.2594, '東都タクシー': 4.1616, '私鉄共同無線': 5.2310, '東個協': 12.6763, '日個連都営協': 9.4040},
]

# データフレームに変換
df = pd.DataFrame(taxi_data)

# 色設定
company_colors = dict(日本交通='#FF6B6B', 東京無線='#4ECDC4', 国際自動車='#45B7D1', 帝都自動車交通='#FFA07A',
                      大和自動車交通='#98D8C8', 荏原交通='#AED581', グリーンキャブ='#81C784', 東都タクシー='#64B5F6',
                      私鉄共同無線='#BA68C8', 東個協='#A1887F', 日個連都営協='#90A4AE')

# ストリームリットアプリケーション
st.title('都心グループ別配車数推移')

# 注記
st.write("※東京交通新聞社による調査記事より抜粋（直近23ヶ月）")
st.write("※2024年6月東都タクシー掲載データなし")
# 月範囲の選択
months = df['month'].tolist()
start_month, end_month = st.select_slider('表示する期間を選択してください', options=months, value=(months[0], months[-1]))

# 選択された月範囲に基づいてデータをフィルタリング
filtered_df = df[(df['month'] >= start_month) & (df['month'] <= end_month)]

# 会社選択
selected_companies = st.multiselect('表示する会社を選択してください', options=list(company_colors.keys()), default=list(company_colors.keys()))

# グラフの表示
if selected_companies:
    fig = px.line(filtered_df, x='month', y=selected_companies, color_discrete_map=company_colors)
    fig.update_layout(yaxis_title='配車数 (万)')
    st.plotly_chart(fig)
else:
    st.write("表示する会社を選択してください。")
