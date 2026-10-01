# convert: "968-Dani, ( Electricti@n );; 36y  "
# into: name: Dani | role: electrician | age:36

info = "968-Dani, ( Electricti@n );; 36y  "
print(info.lower().strip().replace("968-", "name: ")
      .replace(",", " | ")
      .replace("(", "role: ")
      .replace("@", "a")
      .replace(");;", " | age:")
      .replace("y", "")
      )
