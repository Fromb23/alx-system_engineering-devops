#!/usr/bin/env ruby
matches = ARGV[0].scan(/^\d{10}$/)
puts matches.join unless matches.empty?
