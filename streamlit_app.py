import streamlit as st
import folium
from streamlit.components.v1 import html

# Streamlitアプリのタイトル
st.title('大分県のマップ')

# 大分市、大分駅、別府市の座標
coordinates = {
    '金池小学校': [33.23396195,131.6133623],
    'J:COM ホルトホール大分': [33.23056637,	131.6059572],
    '上野ヶ丘中学校': [33.22872924,	131.6126297],
    '大分上野丘高等学校': [33.22155439,	131.6119921],
    'コンパルホール': [33.23534276,	131.611097],
    '（旧）荷揚町小学校体育館': [33.24037861,	131.6079404],
    '長浜小学校': [33.23664069,	131.6185963],
    '（旧）中島小学校': [33.24356839,	131.6078256],
    '浜町保育所': [33.2482074,131.6055533
],
    '碩田学園': [33.24806427,131.6121589
],
    '春日町小学校': [33.24021145,131.5967793
],
    '王子中学校': [33.23606079,	131.5948717
],
    '生石保育所': [33.24314415,	131.5881486
],
    '大分西部公民館': [33.23722617,	131.5899006
],
    '大道小学校': [33.23319584,	131.5999991],
    '西の台小学校': [33.22835292,	131.5847721
],
    '大分西中学校': [33.23553035,	131.578583
],
    '大分西高等学校': [33.23350211,	131.590702
],
    '八幡小学校': [33.2425689,	131.5757366
],
    '神崎小学校': [33.25441022,	131.5451054
],
    '豊府小学校': [33.21686488,	131.6039789
],
    '南大分小学校': [33.21469204,	131.5939104
],
    '南大分公民館': [33.20744067,	131.5927611
],
    '南大分体育館': [33.20890194,	131.6007318
],
    '城南小学校': [33.2157236,	131.5867062
],
    '城南中学校': [33.21308599,	131.5795154
],
    '滝尾小学校': [33.21398088,	131.6327399
],
    '滝尾校区公民館': [33.21669204,	131.628797
],
    '下郡小学校': [33.22890433,	131.6338983
],
    '森岡小学校': [33.20532322,	131.6146626
],
    '大分南部公民館': [33.2019768,	131.6120776
],
    '森岡校区公民館': [33.21092558,	131.6196924
],
    '津留小学校': [33.24074436	,131.6302151
],
    '舞鶴小学校': [33.24698885,	131.6263689
],
    '東大分小学校': [33.24399346,	131.6400992
],
    '城東中学校': [33.23878584,	131.6447921
],
    '日岡小学校': [33.24978017,	131.6589679
],
    '大分東部公民館': [33.2455097,	131.6505714
],
    '桃園小学校': [33.24200344,	131.6691495
],
    '原川中学校': [33.24726478	,131.6641502
],
    '明野東小学校': [33.21848152,	131.6574914
],
    '明野西小学校': [33.22204236,	131.6464665
],
    '明野北小学校': [33.23044492,	131.6556238
],
    '明野中学校': [33.21830742,	131.6509635
],
    '明治明野公民館': [33.22865877,	131.6583656
],
    '鶴崎小学校': [33.23933433,	131.6916493
],
    '鶴崎公民館': [33.24119765,	131.695636
],
    '小中島公民館': [33.24733238,	131.6966441
],
    '三佐小学校': [33.25291125,	131.6802987
],
    '別保小学校': [33.2274459,	131.6855449
],
    '鶴崎中学校': [33.23672349,	131.6867794
],
    '学校法人上東学園もりまち幼稚園': [33.22459097,	131.6769364
],
    '明治小学校': [33.21843548,	131.6656887
],
    '大東中学校': [33.20986185,	131.6751068
],
    '明治北小学校': [33.23357381,	131.6680276
],
    '高田小学校': [33.21103504,	131.6897201
],
    '松岡小学校': [33.18108192,	131.6676308
],
    '川添小学校': [33.20208238,	131.6976476
],
    '宮河内ハイランド公民館': [33.19010692,	131.6999193
],
    '陽光台公民館': [33.22228866,	131.7010222
],
    '上戸次小学校': [33.11242634,	131.6527758
],
    '大塔公民館': [33.11983655,	131.6554627
],
    '大南公民館': [33.15669347,	131.6589014
],
    '判田小学校': [33.1642711,	131.6367842
],
    '判田中学校': [33.16610377,	131.6337276
],
    '判田米良公民館': [33.16044618,	131.6206954
],
    '大分南高等学校': [33.15906346,	131.6304008
],
    'ひばりケ丘公民館':[33.17176588,	131.6395095
],
    '竹中小学校':[33.13973137,	131.653443
],
    '竹中中学校':[33.13372474,	131.6502023
],
    '吉野小学校':[33.11396243,	131.6935025
],
    '吉野中学校':[33.11112787,	131.6938874
],
    '稙田小学校':[33.18358773,	131.5637222
],
    '稙田公民館':[33.18814868,	131.5775093
],
    '稙田西中学校':[33.19056602	,131.5598552
],
    '宗方小学校':[33.20561186,	131.5768305
],
    '下宗方公民館':[33.19903637,	131.5890433
],
    '横瀬小学校':[33.18590589,	131.5415844
],
    '横瀬西小学校':[33.19038454,	131.5320785
],
    '東稙田小学校':[33.18766598,	131.5965278
],
    '田尻小学校':[33.17827927,	131.5902274
],
    '寒田小学校':[33.18413317,	131.6046658
],
    '稙田東中学校':[33.17998435,	131.6118697
],
    '敷戸小学校':[33.19096056,	131.6224244
],
    '鴛野小学校':[33.18393241,	131.6187517
],
    '賀来中学校':[33.20655065,	131.559902
],
    '賀来公民館':[33.20420492,	131.5581584
],
    '大在西小学校':[33.24749118,	131.7081347
],
    '大在小学校':[33.24838231,	131.7195704
],
    '大在中学校':[33.23459407,	131.7218775
],
    '大在公民館':[33.24674975,	131.7236751
],
    '大在浜公民館':[33.24203353,	131.7322384
],
    '坂ノ市小学校':[33.23322335	,131.7570231
],
    '坂ノ市中学校':[33.22913583,	131.7511102
],
    '坂ノ市公民館':[33.22823483	,131.7472775
],
    '細公民館':[33.24148965	,131.7746333
],
    '小佐井小学校':[33.22386693	,131.7468124
],
    '和光こども園':[33.23503148	,131.7422151
],
    '丹生小学校':[33.21490637,	131.7229589
],
    '久土公民館':[33.21439689,	131.7313862
],
    '延命寺公民館':[33.20000939	,131.7068566
],
    'こうざき小学校':[33.23948676,	131.7987455
],
    '（旧）木佐上小学校':[33.21739724,	131.7969027
],
    '（旧）大志生木小学校':[33.24556514,	131.835471
],
    '佐賀関中学校':[33.24936554	,131.8628253
],
    '佐賀関小学校':[33.24592516	,131.8742449
],
    '佐賀関公民館':[33.24907846,	131.8733169
],
    'JX金属 関崎みらい海星館':[33.26558038,	131.8993886
],
    '（旧）一尺屋小学校':[33.20081728,	131.8580458
],
    '野津原小学校':[33.16507082	,131.5300747
],
    '野津原公民館':[33.15901168,	131.5242347
],
    '野津原中学校':[33.15488776	,131.5231026
],
    '（旧）野津原中部小学校':[33.14634182,	131.5100459
],
    '上詰公民館':[33.12290996,	131.4780726
],
    '今市健康増進センター':[33.10764447,	131.4504586
]


    
}

# Foliumマップオブジェクトを作成
m = folium.Map(location=[33.2252, 131.6726], zoom_start=12)

# 各場所にマーカーを追加
for location, coord in coordinates.items():
    folium.Marker(location=coord, popup=location).add_to(m)

# FoliumマップをHTMLとして取得
map_html = m._repr_html_()

# Streamlitでマップを表示
st.components.v1.html(map_html, height=500, width=700)
