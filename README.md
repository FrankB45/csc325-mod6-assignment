# CSC325 - Module 6 - Assignment

## Info

How to run tests:

` pytest test_triangle.py `

## Part 1

An equilateral triangle can never also be right — explain why, in one or two sentences

- An equilateral triangle requires every internal angle to be 60 degrees. A right triangle requires one angle of 90 degrees. Therefore, an equilateral triangle can never be a right triangle. 

## Part 2 - Unit Tests

| Test | Co-pilot suggested? | Accept/Modify/Reject | Why |
|---|---|---|---|
| test_triangle_classify | yes | Reject | Copilot inline suggested an single function to test all aspects of triangle_classify python file. Rejected because it was not descriptive and did not have separate functions for different tests |
|test_invalid_triangles|yes|Modify|Copilot suggested multiple assert statements that all followed the same format, expecting Invalid as a response. Modified to be parameterized. |
|test_equilateral_triangles|yes|Modify|Copilot suggested multiple assert statements that all followed the same format, expecting Invalid as a response. Modified to be parameterized.|
|test_isosceles_triangles|yes|Modify|Copilot suggested multiple assert statements that all followed the same format, expecting Invalid as a response. Modified to be parameterized.|
|test_scalene_triangles|yes|Modify| - Copilot suggested multiple assert statements that all followed the same format, expecting Invalid as a response. Modified to be parameterized. - Copilot included the test (3,4,5) expecting the response "Scalene". This does not match the specification as it should return "Right Scalene" |
|test_right_triangles|no|Modify|Used ChatGPT to identify triangles that match this category. Added the parameterized test manually|

