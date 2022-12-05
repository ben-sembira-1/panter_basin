import time

def play_basin():
  basin_timings = [1, 2, 2, 1, 1, 1, 1, 4, 1, 1]
  for count, timing in enumerate(basin_timings):
      print(f"basi{'n' * timing} {':)' if count % 2 == 0 else '(:'}")
      time.sleep(0.5 * timing)

if __name__ == "__main__":
  play_basin()
