from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-medium')
model = AutoModelForCausalLM.from_pretrained('microsoft/DialoGPT-medium')


def generate_response(user_input):
    input_ids = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors='pt')
    chatbot_output = model.generate(input_ids, max_length=1024, pad_token_id=tokenizer.eos_token_id)
    chatbot_response = tokenizer.decode(chatbot_output[0], skip_special_tokens=True)
    properResponse = str(chatbot_response).split(user_input)[1]
    return properResponse


