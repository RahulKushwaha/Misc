# We increment 
# Shoulder by (2.5 or 5), Bench by 5, Deadlift by 10, Squat by 10
# every month until we cannot do any longer. 

# Current Max(for the last month -> we then add 5 to it).
shoulder_max = 105*0.95
# Increment for this month.
shoulder_max += 5

bench_max = 105*0.95
bench_max += 5

deadlift_max = 110*0.95
deadlift_max += 10

squat_max = 110*0.95
squat_max += 10

exercises = {
  "Shoulder": {
    'weight': shoulder_max,
    'aux': 'Bench'
  },
  "Bench": {
    'weight': bench_max,
    'aux': 'Bench'
  },
  "Deadlift": {
    'weight': deadlift_max,
    'aux': 'Squat'
    },
  "Squat": {
    'weight': squat_max,
    'aux': 'Deadlift'
  }
}

w1 = [
  (0.40, "5"),
  (0.50, "5"),
  (0.60, "5"),
  (0.65, "5"),
  (0.75, "5"),
  (0.85, "5+"), # Try to do 5 or more reps. As many as you can.
  (0.5, "10"),
  (0.6, "10"),
  (0.7, "10")
  ]

w2 = [
  (0.40, "5"),
  (0.50, "5"),
  (0.60, "5"),
  (0.70, "3"),
  (0.80, "3"),
  (0.90, "3+"), # Try to do 3 or more reps. As many as you can.
  (0.6, "10"),
  (0.7, "10"), 
  (0.8, "10"),
]

w3 = [
  (0.40, "5"),
  (0.50, "5"),
  (0.60, "5"),
  (0.75, "5"),
  (0.85, "3"),
  (0.95, "1+"), # Try to do 1 or more reps. As many as you can.
  (0.65, "10"),
  (0.75, "10"),
  (0.85, "10"),
]

w4 = [
  (0.40, "10"),
  (0.50, "10"),
  (0.60, "10"),
]

w = [
  w1,
  w2,
  w3,
  w4
]

for exercise in exercises.keys():
  week = 0
  for w_parts in w:
    counter = 0
    week += 1
    print("Week {}".format(week))
    for d in w_parts:
      counter += 1
      if counter < 7:
        print(exercise, round(d[0] * exercises[exercise]['weight']), "x", d[1])
      else:
        aux = exercises[exercise]['aux']
        print(aux, round(d[0] * exercises[aux]['weight']), "x", d[1])
    print("")
