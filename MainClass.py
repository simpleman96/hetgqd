#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np
import ControlDatabaseAccess as CD
import ControlCalculation as CC


# class MainClass :
# if __name__ == '__main__':
def caculator(student_input):
    # # ********************** GET INPUT FROM STUDENT
    #
    # # Exam blocks choosed by student
    # examGroups = ['A00', 'B00']
    # # Predict marks of all subjects in above exam groups
    # predictSubjects = {}
    #
    # # Subject 1
    # subject = u'Toán'
    # # Calculate the average mark from 5 recent semesters
    # averageMark = CC.averageMark([8.6, 9.0, 8.0, 8.5, 9.0])
    # # The recent college test mark of student
    # collegeTestMark = 8.0
    # # Calculate the bonus when student takes part in competitions hold for excellent students
    # bonusForCompetition = CC.bonusForCompetition(8.0, 2)
    # # Add the set of key (subject) and value (predicted mark) to dictionary predictSubjects
    # predictSubjects.__setitem__(subject,
    #                             CC.predictedMark(averageMark, collegeTestMark, bonusForCompetition))
    #
    # # Subject 2
    # subject = u'Vật Lý'
    # # Calculate the average mark from 5 recent semesters
    # averageMark = CC.averageMark([8.6, 9.0, 8.0, 8.5, 9.0])
    # # The recent college test mark of student
    # collegeTestMark = 8.0
    # # Calculate the bonus when student takes part in competitions hold for excellent students
    # bonusForCompetition = CC.bonusForCompetition(8.0, 2)
    # # Add the set of key (subject) and value (predicted mark) to dictionary predictSubjects
    # predictSubjects.__setitem__(subject,
    #                             CC.predictedMark(averageMark, collegeTestMark, bonusForCompetition))
    #
    # # Subject 3
    # subject = u'Hóa Học'
    # # Calculate the average mark from 5 recent semesters
    # averageMark = CC.averageMark([8.6, 9.0, 8.0, 8.5, 9.0])
    # # The recent college test mark of student
    # collegeTestMark = 8.0
    # # Calculate the bonus when student takes part in competitions hold for excellent students
    # bonusForCompetition = CC.bonusForCompetition(8.0, 2)
    # # Add the set of key (subject) and value (predicted mark) to dictionary predictSubjects
    # predictSubjects.__setitem__(subject,
    #                             CC.predictedMark(averageMark, collegeTestMark, bonusForCompetition))
    #
    # # Subject 4
    # subject = u'Sinh Học'
    # # Calculate the average mark from 5 recent semesters
    # averageMark = CC.averageMark([8.6, 9.0, 8.0, 8.5, 9.0])
    # # The recent college test mark of student
    # collegeTestMark = 8.0
    # # Calculate the bonus when student takes part in competitions hold for excellent students
    # bonusForCompetition = CC.bonusForCompetition(8.0, 2)
    # # Add the set of key (subject) and value (predicted mark) to dictionary predictSubjects
    # predictSubjects.__setitem__(subject,
    #                             CC.predictedMark(averageMark, collegeTestMark, bonusForCompetition))
    #
    # # The favorite levels to groups of subjects
    # subjectFavoriteLevel = [8.0, 1.0, 5.0, 1.0, 8.0, 1.0]
    # # The favorite levels to fields
    # fieldFavoriteLevel = [2.0, 8.0, 9.0, 2.0, 2.0, 2.0, 2.0]
    # # The favorite levels to characters
    # characterFavoriteLevel = [3.0, 3.0, 8.0, 7.0]
    # # The 3 majors liked the most by student
    # favoriteMajors = {u'An toàn thông tin': 8.0, u'Công nghệ chế tạo máy': 7.0, u'Công nghệ thông tin': 8.0}
    # # The 3 colleges liked the most by student
    # favoriteColleges = {u'Đại học Bách khoa Hà Nội': 9.0, u'Trường đại học quốc gia TPHCM': 8.0,
    #                     u'Đại học Kỹ thuật Công Nghiệp - Đại học Thái Nguyên': 6.0}
    # # The tuition fee that student can pay for
    # studentFee = 3
    #
    # # The set of weights represents the target of student
    # userWeights = [0.2, 0.5, 0.15, 0.15]
    examGroups, predictSubjects, subjectFavoriteLevel, fieldFavoriteLevel, characterFavoriteLevel, favoriteMajors, favoriteColleges, studentFee, userWeights = student_input
    # ********************** GET DATA FROM DATABASE

    # Get a dictionary represent the suitable criterion between major and groups of subjects
    typicalSubjectFavority = CD.getDictionaryFromDatabase('nganh_monhoc', ('ten_nganh',), (
        'tu_nhien', 'xa_hoi', 'ngoai_ngu', 'the_duc', 'cong_nghe', 'nang_khieu'))
    # Get a dictionary represent the suitable criterion between major and fields
    typicalFieldFavority = CD.getDictionaryFromDatabase('nganh_linhvuc', ('ten_nganh',), (
        'nhan_van', 'tu_nhien', 'cong_nghe', 'kinh_te', 'y_duoc', 'quoc_phong', 'nang_khieu'))
    # Get a dictionary represent the suitable criterion between major and groups of characters
    typicalCharacterFavority = CD.getDictionaryFromDatabase('nganh_tinhcach', ('ten_nganh',), (
        'thong_tri', 'anh_huong', 'kien_dinh', 'tuan_thu'))
    # Get a dictionary contain the tuition fee of all colleges
    collegeFees = CD.getDictionaryFromDatabase('truong_hocphi', ('ten_truong',), ('muc_hoc_phi',))
    # Get a dictionary contain the job rates of all majors
    jobRates = CD.getDictionaryFromDatabase('nganh_tyle', ('ten_nganh',), ('ty_le',))
    # Get a dictionary contain the rank of all colleges
    collegeRanks = CD.getDictionaryFromDatabase('truong_rank', ('ten_truong',), ('rank',))
    # Get a dictionary contain the subjecs of exam blocks
    dictOfExamBlocks = CD.getDictionaryFromDatabase('khoi_thi', ('ten_khoi',),
                                                                       ('mon_1', 'mon_2', 'mon_3'))
    # Get a dictionary contain standard marks in recent three years
    major_college_examBlock = CD.getDictionaryFromDatabase('nganh_truong_khoi',
                                                                              ('ten_nganh', 'ten_truong', 'ten_khoi'), (
                                                                                  'diem_nam_1', 'diem_nam_2',
                                                                                  'diem_nam_3'))

    # ********************** BUIDING THE MATRIX FOR EVALUATING THE SUITABILITY BETWEEN STUDENT AND CURRENT CHOICE

    # List contain all of choices that can be suitable for student
    listOfChoices = []
    # Filter the choices containing the exam blocks of student
    for key, value in major_college_examBlock.items():
        if key[2] in examGroups:
            # Calculate the average standard mark in recent three years
            officialAverageMark = CC.officialAverageMark(value)
            # Create a list containing major, college, exam block
            choiceList = list(key)
            choiceList.append(officialAverageMark)
            # Add the suitable choice into the listOfChoices
            listOfChoices.append(choiceList)

    # Create a new matrix to evaluate the suitability between student and choices
    matrixForEvaluation = np.zeros((len(listOfChoices), 4), float)
    # Compute the value for all of elements in evaluating matrix
    for choiceIndex in range(len(listOfChoices)):
        # ********************** SUITABILITY OF EXAM MARK

        # Get the exam block of this choice
        examBlock = listOfChoices[choiceIndex][2]
        # Get list of 3 exam subjects in exam block
        listOfSubjects = dictOfExamBlocks.__getitem__((examBlock,))
        # Get predicted marks for 3 exam subjects
        # print listOfSubjects
        # print predictSubjects
        predictedMark1 = predictSubjects[listOfSubjects[0]]
        predictedMark2 = predictSubjects[listOfSubjects[1]]
        predictedMark3 = predictSubjects[listOfSubjects[2]]
        # Compute the total of marks of three exam subjects
        totalOfPredictedMarks = predictedMark1 + predictedMark2 + predictedMark3
        # Get official stardard mark of that exam blocks
        standardMark = listOfChoices[choiceIndex][3]
        # Compute the suitability between the official mark and predicted marks
        matrixForEvaluation[choiceIndex][0] = CC.markSuitability(standardMark, totalOfPredictedMarks)

        # ********************** SUITABILITY OF PEOPLE NATURE

        # Get major of this choice
        major = listOfChoices[choiceIndex][0]
        # Get college of this choice
        college = listOfChoices[choiceIndex][1]

        # Calculate the suitability based on the group of subjects
        subjectSuitability = CC.subjectSuitability(list(typicalSubjectFavority.__getitem__((major,))),
                                                   subjectFavoriteLevel)
        # Calculate the suitability based on the fields
        fieldSuitability = CC.fieldSuitability(list(typicalFieldFavority.__getitem__((major,))),
                                               fieldFavoriteLevel)
        # Calculate the suitability based on the characters
        characterSuitability = CC.characterSuitability(
            list(typicalCharacterFavority.__getitem__((major,))), characterFavoriteLevel)
        # Calculate the suitability of major
        majorSuitability = CC.majorSuitability(favoriteMajors, major)
        # Calculate the suitability of major
        collegeSuitability = CC.collegeSuitability(favoriteColleges, college)
        # Calculate the suitability of people nature
        matrixForEvaluation[choiceIndex][1] = CC.naturalSuitability(subjectSuitability,
                                                                    fieldSuitability,
                                                                    characterSuitability,
                                                                    majorSuitability,
                                                                    collegeSuitability)

        # ********************** SUITABILITY OF TUITION FEE

        # Calculate the suitability of tuition fee
        collegeFee = collegeFees.__getitem__((college,))[0]
        matrixForEvaluation[choiceIndex][2] = CC.feeSuitability(collegeFee, studentFee)

        # ********************** ABILITY FOR DEVELOPING INDIVIDUAL CAREER

        # Calculate the ability for developing individual career
        matrixForEvaluation[choiceIndex][3] = CC.careerDevelopmentSuitability(jobRates, major,
                                                                              collegeRanks, college)

    # ********************** APPLYING THE TOPSIS MODEL FOR ABOVE EVALUATING MATRIX

    ranks = CC.topsisModel(matrixForEvaluation, userWeights)
    print "Ranks For All Choices : "
    print ranks

    # Find the best choice
    maxIndex = 0
    maxRank = ranks[0]
    for index in range(1, ranks.shape[0]):
        if maxRank < ranks[index]:
            maxRank = ranks[index]
            maxIndex = index
    # print '\nThe best choice : ', u'{0}'.format(
    #     listOfChoices[maxIndex][0]), ', Index : ', maxIndex, ', Rank : ', maxRank
    # print '\nThe best choice : ', u'{0}'.format(
    #     listOfChoices[maxIndex][1]), ', Index : ', maxIndex, ', Rank : ', maxRank
    # print '\nThe best choice : ', u'{0}'.format(
    #     listOfChoices[maxIndex][2]), ', Index : ', maxIndex, ', Rank : ', maxRank

    result = [listOfChoices[maxIndex][0:3]]
    return result
