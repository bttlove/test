import streamlit as st
import re
import random
import time

st.set_page_config(page_title="Đăng ký tài khoản", page_icon="🎈")
st.title("Đăng ký tài khoản")

def is_valid_gmail(email):
	# Gmail hợp lệ: chỉ nhận @gmail.com, không ký tự đặc biệt đầu/cuối, không dấu cách
	pattern = r"^[a-zA-Z0-9._%+-]+@gmail\.com$"
	return re.match(pattern, email) is not None

def is_valid_password(password):
	if len(password) < 8:
		return False
	if not re.search(r"[A-Z]", password):
		return False
	if not re.search(r"[a-z]", password):
		return False
	if not re.search(r"[0-9]", password):
		return False
	if not re.search(r"[!@#$%^&*()_+\-=[\]{};':\"\\|,.<>/?]", password):
		return False
	return True

with st.form("register_form"):
	email = st.text_input("Email (Gmail)", placeholder="example@gmail.com")
	password = st.text_input("Mật khẩu", type="password", placeholder="Tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số, ký tự đặc biệt")
	submit = st.form_submit_button("Đăng ký")

if submit:
	if not is_valid_gmail(email):
		st.error("Email của bạn không hợp lệ, vui lòng kiểm tra định dạng.")
	elif not is_valid_password(password):
		st.error("Mật khẩu không chính xác. Yêu cầu: tối thiểu 8 ký tự, gồm chữ hoa, chữ thường, số, ký tự đặc biệt.")
	else:
		st.success("Đăng ký thành công!")
		# Hiệu ứng bong bóng bay
		for _ in range(30):
			x = random.randint(0, 100)
			y = random.randint(0, 100)
			color = random.choice(["#FF69B4", "#87CEEB", "#FFD700", "#32CD32", "#FF4500"])
			st.markdown(f"""
			<div style='position:fixed; left:{x}vw; top:{y}vh; z-index:9999;'>
				<span style='font-size:2.5em; color:{color};'>🎈</span>
			</div>
			""", unsafe_allow_html=True)
			time.sleep(0.03)
		st.balloons()