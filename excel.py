import openpyxl

def save_to_excel(q, a, score, speaker, filename='chat_results.xlsx'):
    """
    将问题、答案、评分、说话人信息保存到 Excel 文件。

    :param q: 问题文本
    :param a: 答案文本
    :param score: GPT 给出的评分
    :param speaker: 识别出的说话人
    :param filename: 保存的文件名，默认为 'chat_results.xlsx'
    """
    # 尝试加载已存在的 Excel 文件，如果不存在则创建一个新的文件
    try:
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
    except FileNotFoundError:
        # 如果文件不存在，则创建新的工作簿
        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "聊天记录"
        # 写入表头
        sheet.append(["问题 (Q)", "回答 (A)", "评分 (Score)", "说话人 (Speaker)"])

    # 将 q, a, score, speaker 写入新的行
    sheet.append([q, a, score, speaker])

    # 保存文件
    workbook.save(filename)
    print(f"数据已写入 {filename} 文件中。")