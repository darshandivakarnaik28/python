Given two strings bound and tag, create a new string by inserting tag in the middle of bound.

The string bound has an even length, so it can be divided into two equal parts. Insert tag between these two parts and return the resulting string.

For example: if bound = "[[]]" and tag = "tag", dividing bound into "[[" and "]]" gives the result [[tag]]..

Examples:

Input: bound = [[]], tag = tag
Output: [[tag]]
Input: bound = <>, tag = body
Output: <body>
Constraints:

1 ≤ bound.size(), tag.size() ≤ 103