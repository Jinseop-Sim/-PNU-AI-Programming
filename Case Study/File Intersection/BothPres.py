def createListFromFile(file):
  infile = open(file, 'r')
  newList = [line.rstrip() for line in infile]
  infile.close()
  return newList

def createNewFile(src_list, src_file, dest_file):
  infile = open(src_file, 'r')
  outfile = open(dest_file, 'w')
  for person in infile:
    if person.rstrip() in src_list: # 공백을 없애고 List와 비교하기 위해 .rstrip() 메서드 사용
      outfile.write(person) # 얘는 File에 Write를 하는 것이므로 공백도 그냥 포함해서 write.
  infile.close()
  outfile.close()

vicepres = createListFromFile("VPres.txt")
createNewFile(vicepres, "USPres.txt", "Both.txt")
