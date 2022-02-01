import re
import json


rgb_keys = ('r', 'g', 'b')
hsl_keys = ('h', 's', 'l')


def parse_data(soup):
    colors = []

    chart_element = soup.find('header', {'id': 'flat'})
    for color_group in chart_element.findAll('div', class_='color-group'):
        for color_element in color_group.findAll('div', class_='js-color'):
            colors.append({
                'hex': color_element['data-hex'].upper(),
                'rgb': get_color_data(color_element['data-rgb'], rgb_keys),
                'hsl': get_color_data(color_element['data-hsl'], hsl_keys)
            })

    return colors


def get_color_data(string, keys):
    values = get_values_from_string(string)
    return {key: value for key, value in zip(keys, values)}


def get_values_from_string(string):
    result = []
    pattern = r'[0-9]+%?'
    matches = re.findall(pattern, string)

    for match in matches:
        result.append(match)

    return result


def write_output(colors):
    with open('colors.json', 'w+') as json_file:
        json.dump(colors, json_file, indent=2)