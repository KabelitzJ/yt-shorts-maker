from generate_content import process_image

def main():
  lines = process_image('./test/tumblr_mjs0wx09on1s8792uo1_1280.png')

  for line in lines:
    print(line)

if __name__ == "__main__":
  main()
