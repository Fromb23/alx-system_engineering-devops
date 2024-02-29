#!/usr/bin/env ruby
if ARGV.length != 1
  puts "wrong number of command line args"
  exit
end

#Get the args
args = ARGV[0]

#Find the regex match
matches = args.scan(/hb*t*n/)

#Print the match
puts matches.join
