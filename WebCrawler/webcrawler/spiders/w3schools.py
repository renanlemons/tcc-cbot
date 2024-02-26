import json
import scrapy
from bs4 import BeautifulSoup
from googletrans import Translator

class W3CSpider(scrapy.Spider):
    name = "w3c"
    start_urls = [
        "https://www.w3schools.com/c/c_intro.php",
        "https://www.w3schools.com/c/c_variables.php",
        "https://www.w3schools.com/c/c_variables_format.php",
        "https://www.w3schools.com/c/c_variables_change.php",
        "https://www.w3schools.com/c/c_variables_multiple.php",
        "https://www.w3schools.com/c/c_variables_names.php",
        "https://www.w3schools.com/c/c_data_types.php",
        "https://www.w3schools.com/c/c_data_types_characters.php",
        "https://www.w3schools.com/c/c_data_types_numbers.php",
        "https://www.w3schools.com/c/c_data_types_dec.php",
        "https://www.w3schools.com/c/c_data_types_sizeof.php",
        "https://www.w3schools.com/c/c_constants.php",
        "https://www.w3schools.com/c/c_operators.php",
        "https://www.w3schools.com/c/c_booleans.php",
        "https://www.w3schools.com/c/c_conditions.php",
        "https://www.w3schools.com/c/c_conditions_else.php",
        "https://www.w3schools.com/c/c_conditions_elseif.php",
        "https://www.w3schools.com/c/c_switch.php",
        "https://www.w3schools.com/c/c_while_loop.php",
        "https://www.w3schools.com/c/c_do_while_loop.php",
        "https://www.w3schools.com/c/c_for_loop.php",
        "https://www.w3schools.com/c/c_for_loop_nested.php",
        "https://www.w3schools.com/c/c_break_continue.php",
        "https://www.w3schools.com/c/c_arrays.php",
        "https://www.w3schools.com/c/c_arrays_size.php",
        "https://www.w3schools.com/c/c_strings.php",
        "https://www.w3schools.com/c/c_strings_esc.php",
        "https://www.w3schools.com/c/c_strings_functions.php",
        "https://www.w3schools.com/c/c_user_input.php",
        "https://www.w3schools.com/c/c_memory_address.php",
        "https://www.w3schools.com/c/c_pointers.php",
        "https://www.w3schools.com/c/c_pointers_arrays.php",
        "https://www.w3schools.com/c/c_functions.php",
        "https://www.w3schools.com/c/c_functions_parameters.php",
        "https://www.w3schools.com/c/c_functions_decl.php",
        "https://www.w3schools.com/c/c_functions_recursion.php",
        "https://www.w3schools.com/c/c_math.php",
        "https://www.w3schools.com/c/c_structs.php"
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        sections = []

        translator = Translator()

        for tag in soup.select('#main h2'):
            # traduz o título para o português
            translated_title = translator.translate(
                tag.text.strip(), dest='pt').text
            
            if translated_title.startswith("Exercício:"):
                translated_title = translated_title.replace("Exercício:", "Exercício_")

            current_dict = {'title': translated_title, 'content': ''}
            next_tag = tag.find_next_sibling()
            while next_tag and next_tag.name != 'hr':
                current_dict['content'] += str(next_tag.get_text(separator=' ', strip=True))
                next_tag = next_tag.find_next_sibling()

            # traduz o conteúdo para o português
            translated_content = translator.translate(
                current_dict['content'], dest='pt').text
            
            # Remove os caracteres de nova linha do conteúdo
            translated_content = translated_content.replace('\n', '')
            current_dict['content'] = translated_content

            # Remove os \"
            translated_content = translated_content.replace('\"', '')
            current_dict['content'] = translated_content

            sections.append(current_dict)

        yield {'sections': sections}

    def closed(self, reason):
        # cria um dicionário com a chave "sections"
        sections_list = []
        for item in self.crawler.stats.get('item_scraped_count', []):
            sections_list.extend(item['sections'])
        result_dict = {'sections': sections_list}

        # converte o dicionário para JSON
        result_json = json.dumps(result_dict)
        self.logger.info(result_json)
        yield json.loads(result_json)
