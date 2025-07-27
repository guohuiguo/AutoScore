# 一个失败的界面，我暂时不能合理得将界面和main函数结合在一起
import tkinter as tk
from tkinter import messagebox
import asr_customization_demo
import gpt
import excel

# 设置音频文件路径
path1 = 'qu.mp3'  # 问题音频路径
path2 = 'a.mp3'   # 回答音频路径

def record_question():
    """录制问题音频"""
    try:
        messagebox.showinfo("录制中", "正在录制问题音频，请稍候...")
        asr_customization_demo.record_audio(path1, duration=5)
        messagebox.showinfo("录制完成", "问题音频录制完成！")
    except Exception as e:
        messagebox.showerror("错误", f"录制问题音频失败：{str(e)}")

def record_answer():
    """录制回答音频"""
    try:
        messagebox.showinfo("录制中", "正在录制回答音频，请稍候...")
        asr_customization_demo.record_audio(path2, duration=5)
        messagebox.showinfo("录制完成", "回答音频录制完成！")
    except Exception as e:
        messagebox.showerror("错误", f"录制回答音频失败：{str(e)}")

def process_and_save():
    """处理音频并保存到 Excel"""
    try:
        # 转写问题音频
        messagebox.showinfo("处理中", "正在转写问题音频...")
        q = asr_customization_demo.asrc_short_example(path1)

        # 转写回答音频
        messagebox.showinfo("处理中", "正在转写回答音频...")
        a = asr_customization_demo.asrc_short_example(path2)

        # GPT 评分
        score = gpt.chat(str(q), str(a))
        score = score.split('：')[1]

        # 保存到 Excel
        excel.save_to_excel(q, a, score)

        # 显示成功保存的消息
        messagebox.showinfo("保存成功", f"问题: {q}\n回答: {a}\n评分: {score}\n已保存到 Excel 文件！")

    except Exception as e:
        messagebox.showerror("错误", f"处理音频失败：{str(e)}")

def create_gui():
    """创建并启动 GUI 界面"""
    # 创建主窗口
    window = tk.Tk()
    window.title("语音问答处理系统")  # 窗口标题
    window.geometry("400x300")  # 窗口大小

    # 创建按钮
    button1 = tk.Button(window, text="录制问题", command=record_question, width=20, height=2, bg="blue", fg="white")
    button2 = tk.Button(window, text="录制回答", command=record_answer, width=20, height=2, bg="green", fg="white")
    button3 = tk.Button(window, text="处理并保存", command=process_and_save, width=20, height=2, bg="red", fg="white")

    # 布局按钮
    button1.pack(pady=20)
    button2.pack(pady=20)
    button3.pack(pady=20)

    # 运行主循环
    window.mainloop()