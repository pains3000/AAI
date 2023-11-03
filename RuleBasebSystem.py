hypothesis(Disease)
write('I believe that the patient has '),
write(Disease), 
nl,
write('TAKE CARE '),
undo
      hypothesis(cold) :- cold, !. 
hypothesis(flu) :- flu, !. 
hypothesis(typhoid) :- typhoid, !. 
hypothesis(measles) :- measles, !. 
hypothesis(malaria) :- malaria, !. 
hypothesis(unknown).

cold :-
    verify(headache), 
    verify(runny_nose), 
    verify(sneezing), 
    verify(sore_throat), 
    write('Advices and Suggestions:'), 
    nl,
    write('1: Tylenol/tab'),
    nl,
    write('2: panadol/tab'), 
    nl,
    write('3: Nasal spray'), 
    nl,
    write('Please wear warm clothes Because'), 
    nl.

flu :-
    verify(fever),
    verify(headache), 
    verify(chills), 
    verify(body_ache),
    write('Advices and Suggestions:'), 
    nl,
    write('1: Tamiflu/tab'), 
    nl,
    write('2: panadol/tab'), 
    nl,
    write('3: Zanamivir/tab'), 
    nl,
    write('Please take a warm bath and do salt gargling Because'), 
    nl.

typhoid :-
    verify(headache), 
    verify(abdominal_pain), 
    verify(poor_appetite), 
    verify(fever),
    write('Advices and Suggestions:'), 
    nl,
    write('1: Chloramphenicol/tab'), 
    nl,
    write('2: Amoxicillin/tab'), 
    nl,
    write('3: Ciprofloxacin/tab'), 
    nl,
    write('4: Azithromycin/tab'), 
    nl,
    write('Please do complete bed rest and take soft Diet Because'), 
    nl.

measles :-
    verify(fever), 
    verify(runny_nose), 
    verify(rash), 
    verify(conjunctivitis),
    write('Advices and Suggestions:'), 
    nl,
    write('1: Tylenol/tab'), 
    nl,
    write('2: Aleve/tab'), 
    nl,
    write('3: Advil/tab'), 
    nl,
    write('4: Vitamin A'), 
    nl,
    write('Please get rest and use more liquid Because'), 
    nl.

malaria :-
    verify(fever), 
    verify(sweating), 
    verify(headache), 
    verify(nausea), 
    verify(vomiting), 
    verify(diarrhea),
    write('Advices and Suggestions:'), 
    nl,
    write('1: Aralen/tab'), 
    nl,
    write('2: Qualaquin/tab'), 
    nl,
    write('3: Plaquenil/tab'), 
    nl,
    write('4: Mefloquine'), 
    nl,
    write('Please do not sleep in open air and cover your full skin Because'), 
    nl.

ask(Question) :-
    write('Does the patient have the following symptom:'), 
    write(Question),
    write('? '), 
    read(Response), 
    nl,
    ( (Response == yes ; Response == y)
    ->
    assert(yes(Question)) ; 
    assert(no(Question)), fail).

:- dynamic yes/1, no/1.

verify(S) :-
    (yes(S)
    ->
    true ; 
    (no(S)
    ->
    fail ; 
    ask(S))).

undo :- retract(yes(_)),fail. 
undo :- retract(no(_)),fail. 
undo.
