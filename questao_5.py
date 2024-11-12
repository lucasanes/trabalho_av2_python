from datetime import datetime
from statistics import mean, multimode

def calculateTimeDurations(filePath):
  times = []
  
  with open(filePath, 'r') as file:
    next(file)
    
    for line in file:
      if not line.strip():
        continue
      
      parts = line.strip().split(',')
      if len(parts) != 2:
        print(f"\nLinha com formato incorreto ignorada: {line.strip()}")
        continue
      
      startTimeStr, endTimeStr = parts
      
      try:
        startTime = datetime.strptime(startTimeStr, "%Y-%m-%d %H:%M:%S")
        endTime = datetime.strptime(endTimeStr, "%Y-%m-%d %H:%M:%S")
      except ValueError:
        print(f"\nErro ao processar linha: {line.strip()}")
        continue
      
      duration = (endTime - startTime).total_seconds() / 60
      times.append(duration)
  
  if not times:
    print("\nArquivo não contém dados válidos.")
    return
  
  minimum = min(times)
  maximum = max(times)
  modes = multimode(times)
  mode = modes[0] if len(modes) == 1 else -1
  average = mean(times)
  
  print(f"Mínimo: {minimum:.1f}")
  print(f"Máximo: {maximum:.1f}")
  print(f"Moda: {mode:.1f}")
  print(f"Média: {average:.1f}")

if __name__ == "__main__":
  calculateTimeDurations("entrada.txt")
