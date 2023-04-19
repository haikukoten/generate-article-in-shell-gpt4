# GPT-4 Blog Post Generator

This repository contains a Python script that uses the OpenAI GPT-4 API and LanguageTool API to generate blog posts on a specified topic.

## Overview

The code leverages the GPT-4 API to generate text based on the user's input for topic and desired word count. It then uses LanguageTool to check and correct any grammar mistakes in the generated text before displaying the final, corrected blog post.

## Setup

1. Install the required packages:
```
pip install requests
pip install language_tool_python
pip install openai
```
2. Replace `your-api-key` with your GPT-4 API key.
3. Change the model if required.
4. Ensure you have a working internet connection, as the script communicates with the GPT-4 and LanguageTool APIs.

## Usage

Run the script using:
```python3 article_generator.py```

You will be prompted to input the desired topic and word count. The script will then generate and display a blog post based on your inputs.

## Customization

You can customize the script to better suit your needs by changing the following parameters:

1. **temperature** (default: 0.8) - Controls the randomness of the generated text. Lower values make the output more focused and deterministic, while higher values make it more creative and diverse.
2. **max_tokens** (default: 3000) - Sets the maximum number of tokens (words) to generate. Adjust this value to limit or extend the length of the generated text.
3. **model** (default: "gpt-4") - Specifies the language model to use. You can change this value to use other available models, such as "gpt-3" or "gpt-3.5-turbo". GPT-4 requires longer time to create content, for faster and cheaper results use gpt-3.5-turbo.
4. **LanguageTool language** (default: "en-US") - Change the language parameter in the LanguageTool constructor to check and correct grammar for other languages supported by LanguageTool.
5. **Change the prompt** - Change the prompt to better suit yours.

## License

This project is released under the custom License. See [LICENSE](https://github.com/haikukoten/generate-article-in-shell-gpt4/blob/main/license.md) for details.
