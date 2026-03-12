with open("text.txt", "w", encoding="utf-8") as f:
    f.write("На Венере одни сутки длятся дольше, чем один год на этой планете.\n")
    f.write("Млечный Путь — это галактика, в которой находится наша Солнечная система.\n")
    f.write("Черные дыры обладают настолько сильной гравитацией, что даже свет не может их покинуть. \n")
    f.write("Четвертая строка, самая длинная из всех, чтобы точно определить максимум.\n")
    f.write("Каждый год на Луну падает около 200 метеоритов, оставляя видимые кратеры.\n")

with open("text.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print(f"Количество строк: {len(lines)}")

words = 0
for line in lines:
    words += len(line.split())
print(f"Количество слов: {words}")

longest = max(lines, key=len).strip()
print(f"Самая длинная строка: {longest}")