#!/usr/bin/env ruby
#Check if an argument was provided
if ARGV.length != 1
  puts "Please provide one argument."
  exit
end

#Get the argument
arg = ARGV[0]

#checks ifthe arg matches the regex
if arg.match(/hbt*n/)
  puts "Match is found."
else
  puts "No match"
end
