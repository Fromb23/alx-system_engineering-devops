#!/usr/bin/env ruby
#check if an argument was provided
if ARGV.length != 1
  puts "please provide one argument."
  exit
end
#Get the argument
arg = ARGV[0]

#check if the argument matches the regular expression
matches = arg.scan(/School/)

#Join the maches into a single string and print it
puts matches.join
