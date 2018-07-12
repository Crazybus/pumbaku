from pumbaku import find_haiku

def test_a_valid_haiku():
    message = find_haiku('An old silent pond. A frog jumps into the pond. Splash silence again')
    assert message == (
        'AN OLD SILENT POND\n'
        'A FROG JUMPS INTO THE POND\n'
        'SPLASH SILENCE AGAIN'
    )

def test_a_valid_haiku_with_new_lines():
    message = find_haiku('An old silent pond.\nA frog jumps into the pond.\nSplash silence again')
    assert message == (
        'AN OLD SILENT POND\n'
        'A FROG JUMPS INTO THE POND\n'
        'SPLASH SILENCE AGAIN'
    )
                       
def test_an_unknown_word():
    message = find_haiku('An old silent crazybus. A frog jumps into the pond. Splash silence again')
    assert message == 'PUMBAKU DO NOT KNOW CRAZYBUS'
                       
def test_not_a_valid_haiku():
    message = find_haiku('haiku')
    assert message == 'HAS 2 SYLLABLES! IS NOT HAIKU!'

def test_not_a_valid_haiku_with_too_many_syllables():
    message = find_haiku('hi ' * 18)
    assert message == 'HAS 18 SYLLABLES! IS NOT HAIKU!'

def test_a_valid_haiku_with_commas():
    message = find_haiku('An old silent pond, A frog jumps into the pond, Splash silence again')
    assert message == (
        'AN OLD SILENT POND\n'
        'A FROG JUMPS INTO THE POND\n'
        'SPLASH SILENCE AGAIN'
    )
