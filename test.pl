# Asking user for Input
print "What is your age?\n";

# Getting an age from the user
$age = <STDIN>;

# Removes new line from the input
chomp $age;

# Printing the value entered by user
print "Your age is ", $age;
