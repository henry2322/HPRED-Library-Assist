class holdsDB:
    # writes ISBN & profile_ID to end of holds.csv
    def request_hold(self, ISBN: int, profile_ID: str):
        with open('holds.csv', 'a') as file:
            file.write('\n' + str(ISBN) + ',' + profile_ID)

    # deletes ISBN & profile_ID from holds.csv
    def cancel_hold(self, ISBN: int, profile_ID: str):
        canceled_hold = str(ISBN) + ',' + profile_ID
        with open('holds.csv', 'r') as file:
            lines = file.readlines()
        with open('holds.csv', 'w') as file2:
            for n in lines:
                if n.strip('\n') != canceled_hold:
                    file2.write(n)

    # prints all ISBN's belonging to profile_ID from holds.csv
    def getHolds(self, profile_ID: str):
        with open('holds.csv', 'r') as file:
            for line in file:
                new_line = line.split(',')[1]
                if new_line.split('\n')[0] == profile_ID:
                    print(line.split(',')[0])
