#!/usr/bin/env ruby
#Check if an argument was provided
if ARGV.length != 1
  puts "Please provide one argument."
  exit
end

#Get the argument
arg = ARGV[0]

#Fidn all matches of the rgex
matches = arg.scan(/hbt+n/)

#print the matches
puts matches.join
