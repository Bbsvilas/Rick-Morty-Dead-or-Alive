import requests
import RandomCharacter

ans = input(f"Is {RandomCharacter.name} dead (Y/N/Hint)?")

if ans == 'Hint':
    print(f'This character is from {RandomCharacter.location}')
    ans = input(f"Is {RandomCharacter.name} dead (Y/N)?")
if ans == 'Y' and RandomCharacter.status == 'Dead' or ans == 'N' and RandomCharacter.status == 'Alive':
    print("You are correct!")

else:
    print(f"That is incorrect")





