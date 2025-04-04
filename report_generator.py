import os
from datetime import datetime

def pass_or_fail(result):
    return "Passou" if result else "Falhou"

def generate_markdown_report_pt(student_name, feedback, test_results):
    # Calculate the score based on the boolean list
    score = sum([25 if result else 0 for result in test_results])

    # Markdown formatted report in Portuguese
    suggestions = []

    # Add suggestions for failed checks only
    if not test_results[0]:  # Branch Principal failed
        suggestions.append("- **Branch Principal**: Certifique-se de fazer o push da `main` branch e verificar se ela existe no seu repositório.")
    if not test_results[1]:  # Presença de Commit failed
        suggestions.append("- **Commits**: Faça commits das suas alterações regularmente. Pelo menos um commit deve ser realizado no seu repositório.")
    if not test_results[2]:  # Existência do Resume.txt failed
        suggestions.append("- **Existência do resume.txt**: Certifique-se de que o arquivo `resume.txt` foi adicionado na raiz do diretório e contém conteúdo significativo.")
    if not test_results[3]:  # Conteúdo do Resume.txt failed
        suggestions.append("- **Conteúdo do Resume**: Garanta que o `resume.txt` contenha pelo menos três linhas com informações relevantes.")

    # Construct the markdown report
    if all(test_results):  # If all checks passed
        feedback_detalhado = "Parabéns! Você passou em todas as verificações. Continue assim, excelente trabalho!"
    else:
        feedback_detalhado = '''
Continue com o bom trabalho! Foque nas áreas mencionadas acima e você terá um desempenho melhor na próxima vez. Não se esqueça de fazer commits regulares no seu repositório!
'''

    report_markdown = f'''
# Relatório de Avaliação para {student_name}

**Pontuação Total**: {score}/100

## Detalhamento da Pontuação:
{feedback}

## Sugestões para Melhoria:
{chr(10).join(suggestions)}

## Feedback Detalhado:
{feedback_detalhado}

---

*Relatório gerado em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
    '''

    return report_markdown

def overwrite_report_in_readme(student_name, feedback, test_results, readme_file="README.md"):
    # Generate the markdown report in Portuguese
    markdown_report = generate_markdown_report_pt(student_name, feedback, test_results)

    # Overwrite the README.md file
    with open(readme_file, "w") as file:
        file.write(markdown_report)

    print(f"Relatório sobrescrito no {readme_file} para {student_name}")

def create_feedback(test_results):
    return f'''
| Verificação               | Pontos | Status |
| ------------------------- | ------ | ------ |
| Branch Principal          | {25 if test_results[0] else 0}     | {pass_or_fail(test_results[0])} |
| Presença de Commit        | {25 if test_results[1] else 0}     | {pass_or_fail(test_results[1])} |
| Existência do Resume.txt  | {25 if test_results[2] else 0}     | {pass_or_fail(test_results[2])} |
| Conteúdo do Resume.txt    | {25 if test_results[3] else 0}     | {pass_or_fail(test_results[3])} |
'''

# Example usage
test_results = [True, True, True, True]  # List of booleans indicating which checks passed or failed
feedback = create_feedback(test_results)
overwrite_report_in_readme("Arthur", feedback, test_results)
