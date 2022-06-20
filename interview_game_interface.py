
import tkinter as tk
from tkinter import messagebox
import random
from gtts import gTTS
from playsound import playsound
import os

root = tk.Tk()
root.title("Interview training [English]")
root.iconbitmap('ICO interview logo.ico')
root.configure(bg="black")

canvas = tk.Canvas(root,width=1080,height=600)
canvas.configure(bg="black")
canvas.grid(columnspan=3, rowspan=6)

'''#logo
logo = Image.open()
logo = Imagetk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row=0)'''

# warning before start
warning_1 = tk.Label(root, text="Before you start, think about the position and company you want to respond to.", font="Raleway", bg="black",fg="white")
warning_1.grid(columnspan=3, column=0,row=0)

# code
def english_interview():
    # https://www.inc.com/jeff-haden/27-most-common-job-interview-questions-and-answers.html
    questions = (
        "Tell me a little about yourself.",
        "What are your biggest weaknesses?",
        "What are your biggest strengths?",
        "Where do you see yourself in five years?",
        "Do you know what is the main task for the jobs?",
        "Out of all the candidates, why should we hire you?",
        "How did you learn about the opening?",
        "Why do you want this job?",
        "What do you consider to be your biggest professional achievement?",
        "Tell me about the last time a co-worker or customer got angry with you. What happened?",
        "Describe your dream job.",
        "Why do you want to leave your current job or why did you resign your last job?",
        "What kind of work environment do you like best?",
        "Tell me about the toughest decision you had to make in the last six months.",
        "What is your leadership style?",
        "Tell me about a time you disagreed with a decision. What did you do?",
        "Tell me how you think other people would describe you.",
        "What can we expect from you in your first three months?",
        "What do you like to do outside of work?",
        "What is your hobbies?",
        "What was your salary in your last job?",
        "What is your salary expectation?",
        "What questions do you have for me?",
        "What do you expect me to accomplish in the first 90 days?",
        "What are the three traits your top performers have in common?",
        "When are you able to start?",
        "Why do you think you are the best candidate?",
        "Why would you like to work in our company?",
        "How do you handle confidential information?",
        "What is your school level?",
        "What really drives results in this job?",
        "What are the company's highest-priority goals this year, and how would my role contribute?"
    )

    language='en'
    question = random.choice(questions)
    question_voice=gTTS(text=question,lang=language)
    question_voice.save("welcome1.mp3")
    playsound("welcome1.mp3")

    msg_box = messagebox.askquestion("Question","Do you wanna hear again?")
    while msg_box == "yes":
        playsound("welcome1.mp3")
        msg_box = messagebox.askquestion("Question","Do you wanna hear again?")
    else:
        messagebox.showinfo("Question",question)

def portuguese_interview():
    # https://www.vagas.com.br/profissoes/perguntas-da-entrevista-de-emprego/
    questions = (
        "Você pode falar um pouco sobre você?",
        "Como você ficou sabendo da vaga?",
        "O que você sabe sobre a empresa?",
        "Por que você quer este trabalho?",
        "Por que devemos contratar você?",
        "Quais são os seus pontos fortes?",
        "Quais são seus pontos fracos?",
        "Qual é a sua maior conquista profissional?",
        "Fale sobre um desafio ou conflito que você enfrentou no trabalho e como você lidou com isso.",
        "Onde você se vê daqui a cinco anos?",
        "Qual é o emprego dos seus sonhos?",
        "Você está se candidatando a vagas de outras empresas?",
        "Por que você está deixando seu emprego atual? ou porque foi demitido?",
        "O que você está procurando em uma nova posição?",
        "Que tipo de ambiente de trabalho você prefere?",
        "Qual o seu estilo de gestão?",
        "Em que situação você exerceu liderança?",
        "Em algum momento você discordou de uma decisão de trabalho? Como foi isso?",
        "Como seu chefe e seus colegas diriam que você é?",
        "Por que existe uma lacuna no seu currículo?",
        "Você pode explicar por que mudou de carreira?",
        "Como você lida com pressões ou situações estressantes?",
        "Quantas bolas de tênis você consegue colocar em uma limusine?",
        "Você tem alguma pergunta?",
        "Qual sua pretensão salarial?",
        "Me fala sobre sua formação escolar."
    )

    language='pt-BR'
    question = random.choice(questions)
    question_voice=gTTS(text=question,lang=language)
    question_voice.save("welcome1.mp3")
    playsound("welcome1.mp3")

    msg_box = messagebox.askquestion("Questão","Você deseja ouvir novamente?")
    while msg_box == "yes":
        playsound("welcome1.mp3")
        msg_box = messagebox.askquestion("Questão","Você deseja ouvir novamente?")
    else:
        messagebox.showinfo("Questão",question)

def spanish_interview():
    # https://www.occ.com.mx/blog/25-preguntas-clave-en-una-entrevista-laboral/
    questions = (
        "Háblame de ti",
        "¿Por qué te interesa el puesto?",
        "¿Qué sabes de nuestra empresa?",
        "¿Qué te gusta hacer en tu tiempo libre?",
        "¿Cuál es tu meta en la vida?",
        "¿Por qué dejaste tu anterior empleo? ¿Por qué quieres cambiar de empleo?",
        "¿Por qué no has durado en tus trabajos anteriores? ¿Por qué duraste tan poco en tu anterior empleo?",
        "¿Por qué te despidieron?",
        "¿Qué me puedes decir de tu jefe anterior?",
        "¿Tienes deudas?",
        "Hay un hueco en tu experiencia laboral ¿qué hiciste durante ese tiempo?",
        "Cuéntame de algún momento de tu vida laboral en el que hayas cometido un error, ¿cómo lo solucionaste?",
        "¿Cómo manejas la presión?",
        "¿Qué pasaría si después de 5 años trabajando con nosotros no obtuvieras un ascenso? ¿Sería frustrante para ti?",
        "¿Cuáles son tus pretensiones salariales?",
        "¿Cuál es tu mayor debilidad o defecto?",
        "¿Cómo describirías tu trabajo ideal?",
        "Si hoy te ganaras la lotería, ¿vendrías a trabajar mañana? ¿Te mueve solo el dinero? ¿Qué tanto respetas tus compromisos?",
        "¿Cómo te ves en 5, 10 años? ¿Coincide el puesto con tus expectativas a futuro?",
        "¿Cuál ha sido el mayor error en tu vida? ¿Qué aprendiste? ¿Aprendes de tus errores? ¿Tus experiencias te ayudaron a madurar?",
        "Háblame de algún reto o conflicto que hayas enfrentado en el trabajo y cómo lo resolviste. ¿Estás preparado para resolver problemas?",
        "Menciona una situación concreta de tu vida laboral en la que hayas demostrado tu liderazgo",
        "¿Cuál es el mayor riesgo que has tomado?",
        "¿Por qué deberíamos contratarte?",
        "¿Tienes alguna pregunta?",
        "¿Qué religión practicas?",
        "¿Cuál es tu orientación sexual?",
        "¿Planeas tener hijos?",
        "¿Padeces alguna enfermedad grave?"
    )

    language='es'
    question = random.choice(questions)
    question_voice=gTTS(text=question,lang=language)
    question_voice.save("welcome1.mp3")
    playsound("welcome1.mp3")

    msg_box = messagebox.askquestion("Pregunta","¿Quieres oír de nuevo?")
    while msg_box == "yes":
        playsound("welcome1.mp3")
        msg_box = messagebox.askquestion("Pregunta","¿Quieres oír de nuevo?")
    else:
        messagebox.showinfo("Pregunta",question)

def german_interview():
    # https://blog.jobchannel.ch/interviewfragen/
    questions = (
        "Erzählen Sie etwas über sich.",
        "Welche persönlichen Ziele haben Sie?",
        "Weshalb wollen Sie sich verändern?",
        "Wo liegen Ihre persönlichen Stärken und Schwächen?",
        "Was bereitet Ihnen besondere Freude?",
        "Womit kann man Sie auf die Palme bringen?",
        "Welche Hobbys haben Sie?",
        "An welchen persönlichen Dingen hängen Sie besonders?",
        "Nehmen Sie aktiv am kulturellen Leben teil?",
        "Als was wollen Sie in der Gesellschaft gesehen werden?",
        "Was schätzen Sie an Ihren Freunden oder Mitarbeitern?",
        "Welche Aufgaben machen Sie gerne, welche weniger?",
        "Was verstehen Sie unter Teamarbeit?",
        "Arbeiten Sie gerne im Team? Halten Sie sich für teamfähig?",
        "Mit welchem Typ Mensch kommen Sie nicht gut aus?",
        "Wie sehen Sie sich selber als Person bezüglich Charakter, Fähigkeiten, Neigungen (Stärken, Schwächen)?",
        "Wie würden Sie sich selbst beschreiben?",
        "Wo sehen Sie Ihre Grenzen?",
        "Wie reagieren Sie auf Kritik von Führungskräften oder Mitarbeitenden?",
        "Arbeiten Sie lieber mit Zahlen oder mit Worten?",
        "Wie verhalten Sie sich unter Termindruck?",
        "Welche Weiterbildung betreiben Sie?",
        "Was haben Sie bisher geleistet?",
        "Was war Ihr schwierigstes berufliches Problem, und wie haben Sie es gelöst?",
        "Welches waren die herausragendsten Leistungen in Ihrer Laufbahn?",
        "Wie verarbeiten Sie Misserfolge?",
        "Wo haben Sie Misserfolge erlebt?",
        "Aus welchen Gründen haben Sie jeweils Ihre Stelle gewechselt?",
        "Welche Ihrer bisherigen Stellen hat Ihnen am besten gefallen? Weshalb?",
        "Was erwarten Sie von der neuen Stelle?",
        "Was sehen Sie sich in 5 oder 10 Jahren? In welcher Position sehen Sie sich dann?",
        "Warum haben Sie sich gerade bei uns beworben?",
        "Por que você está interessado em nossa empresa, nossa indústria, esta posição?",
        "Nennen Sie mir Gründe, weshalb wir ausgerechnet Sie anstellen sollten.",
        "Warum denken Sie, dass Sie sich für die Position qualifizieren?",
        "Was ist Ihre Strategie für die nächsten fünf Jahre?",
        "Weshalb sind Sie arbeitslos geworden?",
        "Wie tief wäre der Minimallohn, zu dem Sie sich anstellen würden?"
    )

    language='de'
    question = random.choice(questions)
    question_voice=gTTS(text=question,lang=language)
    question_voice.save("welcome1.mp3")
    playsound("welcome1.mp3")

    msg_box = messagebox.askquestion("Frage","willst Sie nochmal hören?")
    while msg_box == "yes":
        playsound("welcome1.mp3")
        msg_box = messagebox.askquestion("Frage","willst Sie nochmal hören?")
    else:
        messagebox.showinfo("Frage",question)

#english bottom
en_question_txt = tk.StringVar()
en_question_btn = tk.Button(root, textvariable=en_question_txt, command=lambda:english_interview(), font="Raleway", bg="purple", fg="white", width=20, pady=10)
en_question_txt.set("Question [EN]")
en_question_btn.grid(column=1,row=1)

#portugue bottom
pt_question_txt = tk.StringVar()
pt_question_btn = tk.Button(root, textvariable=pt_question_txt, command=lambda:portuguese_interview(), font="Raleway", bg="purple", fg="white", width=20, pady=10)
pt_question_txt.set("Questão [PT-BR]")
pt_question_btn.grid(column=1,row=2)

#spanish bottom
es_question_txt = tk.StringVar()
es_question_btn = tk.Button(root, textvariable=es_question_txt, command=lambda:spanish_interview(), font="Raleway", bg="purple", fg="white", width=20, pady=10)
es_question_txt.set("Pregunta [ES]")
es_question_btn.grid(column=1,row=3)

#german bottom
ge_question_txt = tk.StringVar()
ge_question_btn = tk.Button(root, textvariable=ge_question_txt, command=lambda:german_interview(), font="Raleway", bg="purple", fg="white", width=20, pady=10)
ge_question_txt.set("Frage [DE]")
ge_question_btn.grid(column=1,row=4)

#donation label
donation_1 = tk.Label(root, text="Independent dev, if you wanna support this and more free softwares: \n paypal: alexismatos1995@gmail.com / pix: loja@desbravei.com", font="Raleway",bg="purple",fg="white")
donation_1.grid(column=1,row=5)

donation_1 = tk.Label(root, text="~nem ganhar, nem perder, mas procurar evoluir~", font="Raleway")
donation_1.grid(column=1,row=6)


root.mainloop()



