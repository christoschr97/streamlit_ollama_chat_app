import streamlit as st
import requests
import json
import config
import pdb


def get_model_response(prompt):
    url = f"{config.API_URL}/generate"
    payload = {
        "model": config.MODEL_NAME,   
        "prompt": prompt,
        "stream": False  
    }
    headers = {"Content-Type": "application/json"}
    
    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()  
        return response.json()  
    except requests.RequestException as e:
        return {"error": str(e)}


# pdb.set_trace()

def main():
    st.title("Local Chat App with Manual Model Server")
    
    st.sidebar.markdown(
        "Make sure you have started the model manually using:\n\n"
        "```\nollama serve\n```"
    )
    
    prompt = st.text_input("Enter your message:")
    if st.button("Send") and prompt:
        result = get_model_response(prompt)
        if "error" in result:
            st.error(f"Error: {result['error']}")
        else:
            st.markdown(f"**Assistant:** {result.get('response', 'No response')}")
    
if __name__ == "__main__":
    main()