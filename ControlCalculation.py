import sys
import numpy as np


# class ControlCalculation:
############################################

# Calculate the average mark of each subject

def averageMark(listOfSemesterAverage):
    # Check whether or not the number of marks in listOfSemesterAverage is equal to 5
    assert (len(listOfSemesterAverage) == 5), "Error : Lack of semester average mark !"

    # Set of the weights for semesters
    semesterWeights = [0.1, 0.1, 0.2, 0.3, 0.3]

    return semesterWeights[0] * listOfSemesterAverage[0] + semesterWeights[1] * listOfSemesterAverage[1] + \
           semesterWeights[2] * listOfSemesterAverage[2] + semesterWeights[3] * listOfSemesterAverage[3] + \
           semesterWeights[4] * listOfSemesterAverage[4]


############################################

# Compute the bonus for students getting prizes in excellent student competition

def bonusForCompetition(mark, rank):
    # rank = 1 : District Level - 0.1   rank = 2 : Province Level - 0.2
    # rank = 3 : National Level - 0.3   rank = 4 : International Level - 0.4
    rankWeights = [0.1, 0.2, 0.3, 0.4]
    return mark * rankWeights[rank - 1]


############################################

# Predict the mark for upcomming college examination

def predictedMark(aver_mark, college_test=0, bonusForCompetition=0):
    # def predictedMark(subject_marks):
    #     aver_mark = averageMark(subject_marks[:5])
    #     college_test = subject_marks[5]
    #     bonusForCompetition = subject_marks[6]
    # Set of the weights for average mark and recent college test mark accordingly
    weights = [0.4, 0.6]
    if college_test == 0:  # when haven't taken part in the college test examination
        return aver_mark + bonusForCompetition
    else:
        return (aver_mark * 0.85) * weights[0] + (college_test * 1.15) * weights[1] + bonusForCompetition


############################################

# Calculate the average standard mark for university enrollment

def officialAverageMark(marksOfThreeYears):
    # Check input parameters
    assert (len(marksOfThreeYears) == 3), "Error : Lack of the stardard marks"
    # Set of the weights for official standard marks of recent three years
    yearWeights = [0.2, 0.3, 0.5]
    return marksOfThreeYears[0] * yearWeights[0] + marksOfThreeYears[1] * yearWeights[1] + marksOfThreeYears[2] * \
                                                                                           yearWeights[2]


############################################

# Calculate the suitability between predicted mark and stardard mark

def markSuitability(standardMark, predictedMark):
    return predictedMark - standardMark


############################################

# Calculate the suitability based on the group of subjects

def subjectSuitability(standardList, userList):
    # Check input parameters
    assert (
        (len(standardList) == len(userList)) and len(userList) == 6), "Error : The input parameters is not valid !"

    standardList = np.array(standardList, float)
    userList = np.array(userList, float)
    return standardList.dot(userList)


############################################

# Calculate the suitability based on fields

def fieldSuitability(standardList, userList):
    # Check input parameters
    assert ((len(standardList) == len(userList)) and len(userList) == 7), "Error : The input parameters is not valid !"

    standardList = np.array(standardList, float)
    userList = np.array(userList, float)
    return standardList.dot(userList)


############################################
# Calculate the suitability based on group of characters

def characterSuitability(standardList, userList):
    # Check input parameters
    assert (
        (len(standardList) == len(userList)) and len(userList) == 4), "Error : The input parameters is not valid !"

    standardList = np.array(standardList, float)
    userList = np.array(userList, float)
    return standardList.dot(userList)


############################################

# Calculate the suitability of major

def majorSuitability(dictForFavoriteMajors, currentMajor):
    defaultFavoriteLevel = 5
    if (currentMajor in dictForFavoriteMajors.keys()):
        return dictForFavoriteMajors.get(currentMajor)
    else:
        return defaultFavoriteLevel


############################################

# Calculate the suitability of college

def collegeSuitability(favoriteCollegeDict, currentCollege):
    defaultFavoriteLevel = 5
    if (currentCollege in favoriteCollegeDict.keys()):
        return favoriteCollegeDict.get(currentCollege)
    else:
        return defaultFavoriteLevel


############################################

# Calculate the suitability of people nature

def naturalSuitability(subjectSuitability, fieldSuitability, characterSuitability, majorSuitability,
                       collegeSuitability):
    weights = [0.15, 0.14, 0.12, 0.3, 0.29]
    return weights[0] * subjectSuitability + weights[1] * fieldSuitability + weights[2] * characterSuitability + \
           weights[3] * majorSuitability + weights[4] * collegeSuitability


############################################
# Calculate the suitability of tuition fee

def feeSuitability(collegeFee, userFee):
    return userFee - collegeFee


############################################

# Calculate the ability for developing individual career

def careerDevelopmentSuitability(jobRates, currentMajor, collegeRanks, currentCollege):
    weights = [0.58, 0.42]
    rateOfJob = jobRates.__getitem__((currentMajor,))[0]
    rankOfCollege = collegeRanks.__getitem__((currentCollege,))[0]
    return weights[0] * rateOfJob + weights[1] * (100 - rankOfCollege + 1)


############################################

# Using Topsis Model for finding out the best choice

def topsisModel(dataMatrix, weightsOfUser):
    dataMatrix = np.array(dataMatrix, float)

    # Find maximum value in each column
    maxOnColumns = np.max(dataMatrix, 0)

    # Normalize all elements in this matrix into range [0, 1]
    dataMatrix = np.divide(dataMatrix, maxOnColumns)  # or : dataMatrix = dataMatrix/maxOnColumns

    # Multiply weights with columns correspondingly
    dataMatrix = np.array(dataMatrix).__imul__(weightsOfUser)  # or : dataMatrix = dataMatrix * weightsOfUser

    # Find out the best choice and worst choice
    bestSelection = np.max(dataMatrix, 0)
    worstSelection = np.min(dataMatrix, 0)

    # Compute the distance between current choice with best choice and worst choice
    bestDistances = np.linalg.norm(dataMatrix - bestSelection, axis=1)
    worstDistances = np.linalg.norm(dataMatrix - worstSelection, axis=1)

    # Find rank for each choice
    ranks = (worstDistances) / (worstDistances + bestDistances)
    return ranks


def normalize(list_input):
    np_input = np.array(list_input, dtype=np.float32)
    np_input /= np.sum(np_input)
    return np_input.tolist()
