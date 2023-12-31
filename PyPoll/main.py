#import libraries
import os
import csv

#Establish path.
csvpath=os.path.join('Resources','election_data.csv')

#Start editing/open the csv file
with open(csvpath)as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)


#Sequester the header, establish a list called candidate list, set candidate count to zero, set total votes and all candidate votes to zero
    header=next(csvreader)
    candidate_list=[]
    total_votes=0
    first_candidate_votes=0
    second_candidate_votes=0
    third_candidate_votes=0


#Start the loop. Have it check if the candidate's name is in the candidate list, if it is not, add the candidate to the list and add one to the vote count, if it is, add one to the vote counter.
    for row in csvreader:
      if row[2] not in candidate_list:
            candidate_list+=[row[2]]
            total_votes+=1
      elif row[2] in candidate_list:
            total_votes+=1 

#Start looping through the rows and compare the candidate name to the index position of the candidate and add a vote to whichever candidate's name matches.
      if row[2]==candidate_list[0]:
           first_candidate_votes+=1
      elif row[2]==candidate_list[1]:
           second_candidate_votes+=1
      elif row[2]==candidate_list[2]:
            third_candidate_votes+=1

#Count how many candidates are in the candidate list.
print(len(candidate_list))

#Define the percent function.
def percent(number):
     return (number/total_votes)*100

#Set values for percent variables and have it round to three decimal places.
percent_first=round(percent(first_candidate_votes),3)
percent_second=round(percent(second_candidate_votes),3)
percent_third=round(percent(third_candidate_votes),3)

#Print the election information in the terminal.
print('Election Results')
print("Total Votes: ",total_votes)
print(candidate_list[0],': ',percent_first,"%","(",first_candidate_votes,")")
print(candidate_list[1],': ',percent_second,"%","(",second_candidate_votes,")")
print(candidate_list[2],': ',percent_third,"%","(",third_candidate_votes,")")

#Set a variable to store the highest votes a candidate got.
winner=max(first_candidate_votes,second_candidate_votes,third_candidate_votes)

#Print the name of the winner to the terminal and store the name of the candidate in the variable election_winner.
if winner==first_candidate_votes:
      print("Winner: ",candidate_list[0])
      election_winner=candidate_list[0]
elif winner==second_candidate_votes:
      print("Winner: ",candidate_list[1])
      election_winner=candidate_list[1]
elif winner==third_candidate_votes:
      print("Winner: ",candidate_list[2])
      election_winner=candidate_list[2]

#Set the output path for the new file.
output_path=os.path.join('Analysis','Analysis_pypoll.txt')

#Write the election information to the analysis_pypoll.txt file.
with open (output_path,'w') as txtfile:
        txtfile.write('Election Results')
        txtfile.write('\n')
        txtfile.write('----------------------------')
        txtfile.write('\n')
        txtfile.write('Total Votes: ')
        txtfile.write(str(total_votes))
        txtfile.write('\n')
        txtfile.write('----------------------------')
        txtfile.write('\n')
        txtfile.write(candidate_list[0])
        txtfile.write(': ')
        txtfile.write(str(percent_first))
        txtfile.write('% (')
        txtfile.write(str(first_candidate_votes))
        txtfile.write(')')
        txtfile.write('\n')
        txtfile.write(candidate_list[1])
        txtfile.write(': ')
        txtfile.write(str(percent_second))
        txtfile.write('% (')
        txtfile.write(str(second_candidate_votes))
        txtfile.write(')')
        txtfile.write('\n')
        txtfile.write(candidate_list[2])
        txtfile.write(': ')
        txtfile.write(str(percent_third))
        txtfile.write('% (')
        txtfile.write(str(third_candidate_votes))
        txtfile.write(')')
        txtfile.write('\n')
        txtfile.write('----------------------------')
        txtfile.write('\n')
        txtfile.write("Winner: ")
        txtfile.write(election_winner)
        txtfile.write('\n')
        txtfile.write('----------------------------')
