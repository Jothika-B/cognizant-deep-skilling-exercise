// MongoDB Aggregation Pipeline (2 Stages)

db.students.aggregate([
  {
    $match: {
      marks: { $gte: 80 }
    }
  },
  {
    $project: {
      name: 1,
      marks: 1,
      _id: 0
    }
  }
]);

Sample Input:
{ "name": "John", "marks": 85 }
{ "name": "Anna", "marks": 72 }
{ "name": "Sam", "marks": 90 }

Output:
{ "name": "John", "marks": 85 }
{ "name": "Sam", "marks": 90 }
