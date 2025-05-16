import random
import sys
"""
Bash Implementation:

words=($(grep '^\w\w\w\w\w$' /usr/share/dict/words | tr '[a-z]' '[A-Z]'))
actual=${words[$[$RANDOM % ${#words[@]}]]} end=false guess_count=0 max_guess=6
if [[ $1 == "unlimit" ]]; then
    max_guess=999999
fi

Python Implementation:
"""

words = []
with open('/usr/share/dict/words', 'r') as f:
    for line in f:
        if len(line.strip()) == 5:
            words.append(line.strip().upper())

actual = words[random.randint(0, len(words) - 1)]
max_guess = 0
if len(sys.argv) > 1 and sys.argv[1] == 'unlimit':
    max_guess = 999999

""" Bash Implementation:
while [[ $end != true ]]; do
    guess_count=$(( $guess_count + 1 ))
    if [[ $guess_count -le $max_guess ]]; then
        echo "Enter your guess ($guess_count / $max_guess):"
        read guess
        guess=$(echo $guess | tr '[a-z]' '[A-Z]')
        if [[ " ${words[*]} " =~ " $guess " ]]; then
            output="" remaining=""
            if [[ $actual == $guess ]]; then
                echo "You guessed right!"
                for ((i = 0; i < ${#actual}; i++)); do
                    output+="\033[30;102m ${guess:$i:1} \033[0m"
                done
                printf "$output\n"
                end=true
            else
                for ((i = 0; i < ${#actual}; i++)); do
                    if [[ "${actual:$i:1}" != "${guess:$i:1}" ]]; then
                        remaining+=${actual:$i:1}
                    fi
                done
                for ((i = 0; i < ${#actual}; i++)); do
                    if [[ "${actual:$i:1}" != "${guess:$i:1}" ]]; then
                        if [[ "$remaining" == *"${guess:$i:1}"* ]]; then
                            output+="\033[30;103m ${guess:$i:1} \033[0m"
                            remaining=${remaining/"${guess:$i:1}"/}
                        else
                            output+="\033[30;107m ${guess:$i:1} \033[0m"
                        fi
                    else
                        output+="\033[30;102m ${guess:$i:1} \033[0m"
                    fi
                done
                printf "$output\n"
            fi
        else
            echo "Please enter a valid word with 5 letters!";
            guess_count=$(( $guess_count - 1 ))
        fi
    else
        echo "You lose! The word is:"
        echo $actual
        end=true
    fi
done

Python Implementation:
"""
guess_count = 0
max_guess = 6
while True:
    guess_count += 1
    if guess_count <= max_guess:
        print("Enter your guess ({} / {}):".format(guess_count, max_guess))
        guess = input()
        guess = guess.upper()
        if guess in words:
            output = ""
            remaining = ""
            if actual == guess:
                print("You guessed right!")
                for i in range(len(actual)):
                    output += "\033[30;102m {} \033[0m".format(guess[i])
                print(output)
                break
            else:
                for i in range(len(actual)):
                    if actual[i] != guess[i]:
                        remaining += actual[i]
                for i in range(len(actual)):
                    if actual[i] != guess[i]:
                        if remaining.find(guess[i]) != -1:
                            output += "\033[30;103m {} \033[0m".format(guess[i])
                            remaining = remaining.replace(guess[i], "")
                        else:
                            output += "\033[30;107m {} \033[0m".format(guess[i])
                    else:
                        output += "\033[30;102m {} \033[0m".format(guess[i])
                print(output)
        else:
            print("Please enter a valid word with 5 letters!")
            guess_count -= 1
    else:
        print("You lose! The word is:")
        print(actual)
        break

