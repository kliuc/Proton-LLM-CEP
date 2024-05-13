import google.generativeai as genai
import os


# configure Gemini AI
API_KEY = os.environ.get('GEMINI_AI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest') # model with faster api limit: gemini-1.0-pro-latest


def check_palindrome(sequence):
    prompt = f'''## Context
A palindrome is a sequence of three characters that reads the same backward as forward.
Here are some examples of palindromes:
- aaa
- aba
- bcb
Here are some non-examples of palindromes:
- a
- bb
- aab
- bcc
- abc

## Task
Given a sequence of characters, identify if the sequence is a palindrome.

## Target sequence
{sequence}

## Output format
If the sequence is a palindrome, respond with "True".
If the sequence is not a palindrome, respond with "False".'''
    
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=5,
            temperature=0
        )
    )
    
    return response.text.strip() == 'True'


if __name__ == '__main__':
    print(check_palindrome('aba'))