import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor.
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo.
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

#This statement finds and counts the non-alphanumerics in the string assigned to 'lorem_ipsum'
#Here we set the pattern in the string
pattern=re.compile('[^0-9a-zA-Z\d]')
#Now we find the pattern in the string
results=pattern.findall(lorem_ipsum)
#This is where we print the length with the len() function
print(len(results))

#Here we set the pattern again
pattern = re.compile('sit-amet|sit:amet')
#Now we store the output to a varible called 'occurrance_sit_amet'
occurrences_sit_amet = pattern.findall(lorem_ipsum)
#Again, we print the length with the len() function
print(len(occurrences_sit_amet))

#Now we replace sit:amet and sit-amet with sit amet using the sub function
#Here we store the output to a variable named 'replace_results'
replace_results=re.sub(pattern,"sit amet",lorem_ipsum)
#This function finds all occurances of 'sit amet' in the string assigned to 'replace_results'
regex="sit[\s]amet"
#Now we store the output to a varible called 'occurrance_sit_amet'
occurrence_sit_amet=re.findall(regex,replace_results)
#Again, we print the length with the len() function
print(len(occurrence_sit_amet))