import streamlit as st
import folium
from streamlit_folium import st_folium

# Streamlitアプリのタイトル
st.title('Streamlitで作成するマップ')

# 地図の初期位置とズームレベルを設定
map_center = [35.6895, 139.6917]  # 東京の緯度経度
zoom_level = 12

# Foliumマップオブジェクトを作成
m = folium.Map(location=map_center, zoom_start=zoom_level)

# マップにマーカーを追加
folium.Marker(location=map_center, popup='東京').add_to(m)

# Streamlitでマップを表示
st_folium(m, width=700, height=500)
