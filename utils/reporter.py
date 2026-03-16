import json
from datetime import datetime

class ReportGenerator:
    def __init__(self, results):
        self.results = results
        self.timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    def generate_html(self):
        html_content = f'<!DOCTYPE html>\n<html>\n<head><title>Scan Report</title></head>\n<body>\n<h1>Scan Report</h1>\n<p>Generated on: {self.timestamp}</p>\n<ul>'
        for result in self.results:
            html_content += f'<li>{result}</li>'
        html_content += '</ul>\n</body>\n</html>'
        return html_content

    def generate_json(self):
        return json.dumps({
            'timestamp': self.timestamp,
            'results': self.results
        }, indent=4)

    def generate_text(self):
        text_content = f'Scan Report\nGenerated on: {self.timestamp}\n\n'
        for result in self.results:
            text_content += f'- {result}\n'
        return text_content

# Example usage
# results = ['Scan 1: No issues found', 'Scan 2: Minor issues detected']
# report_gen = ReportGenerator(results)
# print(report_gen.generate_html())
# print(report_gen.generate_json())
# print(report_gen.generate_text())
