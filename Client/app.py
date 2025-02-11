import streamlit as st
import pickle

mobile_list = pickle.load(open('./mobiles.pkl', 'rb'))
similarity = pickle.load(open('./similarity.pkl', 'rb'))
mobile_list_names = mobile_list['name'].values

st.title('Mobile Recommendation System')

selected_mobile = st.selectbox(
    "Select a Mobile",
    mobile_list_names,
)

# recommend function
def recommend(mobile):
    mobile_index = mobile_list[mobile_list['name'] == mobile].index[0]
    distances = similarity[mobile_index]
    mobile_list_sorted = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]

    recommend_mobiles = []
    mobile_images = []
    for i in mobile_list_sorted:
        mobile_id = i[0]
        recommend_mobiles.append(mobile_list.iloc[mobile_id]["name"])
        mobile_images.append(mobile_list.iloc[mobile_id]["imgURL"])
    
    return recommend_mobiles, mobile_images



if st.button("Recommend", type="secondary"):
    names,images = recommend(selected_mobile)

    cols = st.columns(len(names))  # Create columns dynamically

    for i, col in enumerate(cols):
        with col:
            st.markdown(f"<p style='text-align:center; font-size:18px; font-weight:bold;'>{names[i]}</p>", unsafe_allow_html=True)
            st.image(images[i], width=160, use_container_width=False)  # Adjust image width


st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 50%;
            transform: translateX(-50%);
            width: 100%;
            background-color: #0E1117;
            color: white;
            text-align: center;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            border-top: 2px solid #FF4B4B;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .footer span {
            color: #FF4B4B;
            font-weight: bold;
        }
    </style>
    <div class="footer">
        © <span>&nbsp;Tarun Prajapati</span>
    </div>
""", unsafe_allow_html=True)
