KEYS = (
'*-', 'S-', 'T-', 'K-', 'H-', 'I-', 'A-', 'O-', 't-', 'r-', 's-', 'n-',
'#',
'-*', '-S', '-T', '-K', '-H', '-I', '-A', '-O', '-t', '-r', '-s', '-n',
)

IMPLICIT_HYPHEN_KEYS = ('#')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*-')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Keyboard': {
        '*-' : 'q',
        'S-' : 'a',
        'T-' : 'w',
        'K-' : 's',
        'H-' : 'e',
        'I-' : 'd',
        'A-' : 'c',
        'O-' : 'v',
        't-' : 'r',
        'r-' : 'f',
        's-' : 't',
        'n-' : 'g',
        '#'  : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        '-*' : 'p',
        '-S' : ';',
        '-T' : 'o',
        '-K' : 'l',
        '-H' : 'i',
        '-I' : 'k',
        '-A' : 'm',
        '-O' : 'n',
        '-t' : 'u',
        '-r' : 'j',
        '-s' : 'y',
        '-n' : 'h',
        'arpeggiate': 'space',
        }
        }

DICTIONARIES_ROOT = 'asset:plover_japanese_hachidori:dictionaries'
DEFAULT_DICTIONARIES = ('kana.json')
