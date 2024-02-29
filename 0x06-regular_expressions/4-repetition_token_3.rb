#!/usr/bin/env ruby
matches = ARGV[0].scan(/hbt+n/)
puts matches.join unless matches.empty?
