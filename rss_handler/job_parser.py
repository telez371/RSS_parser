from bs4 import BeautifulSoup
import re


def format_html_for_display(html_title, html_content, content_link):
    try:
        html_parser = BeautifulSoup(html_content, 'html.parser')
        bold_tags = html_parser.find_all('b')

        content_dict = {"Title": html_title}

        plain_text_description = html_parser.get_text()
        if len(plain_text_description) > 200:
            content_dict["Description"] = f"{plain_text_description[:150]}  ...."
        else:
            content_dict["Description"] = plain_text_description

        for bold_tag in bold_tags:
            if bold_tag.next_sibling:
                sibling_text = ' '.join(bold_tag.next_sibling.strip().split())
                if sibling_text:
                    content_dict[bold_tag.text.strip()] = sibling_text

        content_dict["Link"] = content_link

        formatted_result = [f"{key}: {value}" for key, value in content_dict.items()]

        return '\n'.join(formatted_result)
    except Exception:
        return f"{html_title}\nUnable to format description. Link: {content_link}"


def prepare_text_for_gpt(html_content):
    try:
        html_parser = BeautifulSoup(html_content, 'html.parser')
        prepared_text = []

        for bold_tag in html_parser.find_all('b'):
            bold_tag.decompose()

        plain_text_description = html_parser.get_text()
        concise_description = ' '.join(re.split(r'(?<=[.:;])\s', plain_text_description)[:3])
        prepared_text.append(f"Description: {concise_description}...")

        return '\n'.join(prepared_text)
    except Exception as e:
        return f"Error processing HTML content: {e}\nOriginal content: {html_content}"
