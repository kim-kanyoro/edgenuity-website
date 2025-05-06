import streamlit as st
from datetime import datetime

# Set page config
st.set_page_config(
    page_title="Edgenuity by Kimani",
    page_icon="📚",
    layout="wide"
)

# Custom CSS for Instagram-like look & responsive design
st.markdown("""
<style>
body {
    font-family: 'Segoe UI', sans-serif;
}

.container {
    max-width: 700px;
    margin: auto;
    padding: 20px;
}

.profile-header {
    display: flex;
    align-items: center;
    gap: 15px;
    margin-bottom: 20px;
}

.profile-pic {
    width: 90px;
    height: 90px;
    border-radius: 50%;
    border: 3px solid #6a0dad;
}

.username {
    font-size: 24px;
    font-weight: 600;
    color: #6a0dad;
}

.follow-button {
    background-color: #6a0dad;
    color: white;
    padding: 8px 16px;
    border-radius: 6px;
    text-decoration: none;
    font-size: 16px;
}

.follow-button:hover {
    background-color: #4b0082;
}

.post-box {
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    padding: 15px;
    margin-top: 20px;
}

.post-box img {
    width: 100%;
    border-radius: 10px;
    margin-top: 10px;
}

.contact-box {
    background-color: #f5f5f5;
    border-radius: 10px;
    padding: 15px;
    margin-top: 30px;
    text-align: center;
}

.contact-box h3 {
    color: #6a0dad;
}

.footer {
    margin-top: 40px;
    text-align: center;
    font-size: 14px;
    color: #888;
}
</style>
""", unsafe_allow_html=True)

# Website Content
st.markdown('<div class="container">', unsafe_allow_html=True)

# Profile header
st.markdown("""
<div class="profile-header">
    <img src="https://via.placeholder.com/90x90.png?text=Ed" class="profile-pic">
    <div>
        <div class="username">@edgenuity_by_kimani</div>
        <a class="follow-button" href="https://www.instagram.com/edgenuity_by_kimani" target="_blank">Follow</a>
    </div>
</div>
""", unsafe_allow_html=True)

# Post Box
st.markdown('<div class="post-box">', unsafe_allow_html=True)
st.subheader("Simplifying Online Learning 📘")

st.write("""
I specialize in helping students with Edgenuity, Apex, and Edmentum classes at high school, college, and university levels. 
I also assist with essays and assignments at affordable prices. 
Let’s simplify your online learning journey together!
""")

# Show the image (make sure it's in assets/ folder)
try:
    st.image("assets/edg.jpg", caption="Helping students simplify their learning!", use_column_width=True)
except:
    st.warning("⚠️ Image not found. Please place your image as 'edg.JPG' inside the 'assets/' folder.")

st.markdown('</div>', unsafe_allow_html=True)

# Contact Info
st.markdown('<div class="contact-box">', unsafe_allow_html=True)
st.markdown("### Get in Touch")
st.markdown("📞 **Phone**: +19146078458")
st.markdown("📧 **Email**: kimanikanyoro4@gmail.com")
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown(f"""
<div class="footer">
    &copy; {datetime.now().year} Edgenuity by Kimani. All rights reserved.
</div>
</div>
""", unsafe_allow_html=True)
