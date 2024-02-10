// Generated from c://Users//lenovo//Desktop//Compiler Midterm//tamrin3//gram.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class gramLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, IF=6, WHILE=7, INT=8, BOOL=9, 
		ID=10, INTTYPE=11, BOOLTYPE=12, SC=13, WS=14, RELOP=15, EQ=16, COMMENT=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "IF", "WHILE", "INT", "BOOL", 
			"ID", "INTTYPE", "BOOLTYPE", "SC", "WS", "RELOP", "EQ", "COMMENT", "LETTER", 
			"DIGIT"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "'if'", "'while'", "'int'", 
			"'boolean'", null, null, null, "';'", null, null, "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, "IF", "WHILE", "INT", "BOOL", "ID", 
			"INTTYPE", "BOOLTYPE", "SC", "WS", "RELOP", "EQ", "COMMENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public gramLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "gram.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0011|\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002"+
		"\u0012\u0007\u0012\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b"+
		"\u0001\t\u0001\t\u0001\t\u0005\tJ\b\t\n\t\f\tM\t\t\u0001\n\u0003\nP\b"+
		"\n\u0001\n\u0004\nS\b\n\u000b\n\f\nT\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0003\u000b`\b\u000b\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0003\u000el\b\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0004\u0010"+
		"s\b\u0010\u000b\u0010\f\u0010t\u0001\u0010\u0001\u0010\u0001\u0011\u0001"+
		"\u0011\u0001\u0012\u0001\u0012\u0000\u0000\u0013\u0001\u0001\u0003\u0002"+
		"\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013"+
		"\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"#\u0000%\u0000\u0001\u0000\u0004\u0003\u0000\t\n\r\r  \u0002\u0000\n\n"+
		"\r\r\u0003\u0000AZ__az\u0001\u000009\u0081\u0000\u0001\u0001\u0000\u0000"+
		"\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000"+
		"\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000"+
		"\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000"+
		"\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000"+
		"\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000"+
		"\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000"+
		"\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0001\'"+
		"\u0001\u0000\u0000\u0000\u0003)\u0001\u0000\u0000\u0000\u0005+\u0001\u0000"+
		"\u0000\u0000\u0007-\u0001\u0000\u0000\u0000\t/\u0001\u0000\u0000\u0000"+
		"\u000b1\u0001\u0000\u0000\u0000\r4\u0001\u0000\u0000\u0000\u000f:\u0001"+
		"\u0000\u0000\u0000\u0011>\u0001\u0000\u0000\u0000\u0013F\u0001\u0000\u0000"+
		"\u0000\u0015O\u0001\u0000\u0000\u0000\u0017_\u0001\u0000\u0000\u0000\u0019"+
		"a\u0001\u0000\u0000\u0000\u001bc\u0001\u0000\u0000\u0000\u001dk\u0001"+
		"\u0000\u0000\u0000\u001fm\u0001\u0000\u0000\u0000!p\u0001\u0000\u0000"+
		"\u0000#x\u0001\u0000\u0000\u0000%z\u0001\u0000\u0000\u0000\'(\u0005(\u0000"+
		"\u0000(\u0002\u0001\u0000\u0000\u0000)*\u0005)\u0000\u0000*\u0004\u0001"+
		"\u0000\u0000\u0000+,\u0005{\u0000\u0000,\u0006\u0001\u0000\u0000\u0000"+
		"-.\u0005}\u0000\u0000.\b\u0001\u0000\u0000\u0000/0\u0005=\u0000\u0000"+
		"0\n\u0001\u0000\u0000\u000012\u0005i\u0000\u000023\u0005f\u0000\u0000"+
		"3\f\u0001\u0000\u0000\u000045\u0005w\u0000\u000056\u0005h\u0000\u0000"+
		"67\u0005i\u0000\u000078\u0005l\u0000\u000089\u0005e\u0000\u00009\u000e"+
		"\u0001\u0000\u0000\u0000:;\u0005i\u0000\u0000;<\u0005n\u0000\u0000<=\u0005"+
		"t\u0000\u0000=\u0010\u0001\u0000\u0000\u0000>?\u0005b\u0000\u0000?@\u0005"+
		"o\u0000\u0000@A\u0005o\u0000\u0000AB\u0005l\u0000\u0000BC\u0005e\u0000"+
		"\u0000CD\u0005a\u0000\u0000DE\u0005n\u0000\u0000E\u0012\u0001\u0000\u0000"+
		"\u0000FK\u0003#\u0011\u0000GJ\u0003#\u0011\u0000HJ\u0003%\u0012\u0000"+
		"IG\u0001\u0000\u0000\u0000IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000"+
		"\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000L\u0014\u0001"+
		"\u0000\u0000\u0000MK\u0001\u0000\u0000\u0000NP\u0005-\u0000\u0000ON\u0001"+
		"\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000\u0000"+
		"QS\u0003%\u0012\u0000RQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000"+
		"TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000\u0000U\u0016\u0001\u0000"+
		"\u0000\u0000VW\u0005T\u0000\u0000WX\u0005r\u0000\u0000XY\u0005u\u0000"+
		"\u0000Y`\u0005e\u0000\u0000Z[\u0005F\u0000\u0000[\\\u0005a\u0000\u0000"+
		"\\]\u0005l\u0000\u0000]^\u0005s\u0000\u0000^`\u0005e\u0000\u0000_V\u0001"+
		"\u0000\u0000\u0000_Z\u0001\u0000\u0000\u0000`\u0018\u0001\u0000\u0000"+
		"\u0000ab\u0005;\u0000\u0000b\u001a\u0001\u0000\u0000\u0000cd\u0007\u0000"+
		"\u0000\u0000de\u0001\u0000\u0000\u0000ef\u0006\r\u0000\u0000f\u001c\u0001"+
		"\u0000\u0000\u0000gl\u0005<\u0000\u0000hi\u0005=\u0000\u0000il\u0005="+
		"\u0000\u0000jl\u0005>\u0000\u0000kg\u0001\u0000\u0000\u0000kh\u0001\u0000"+
		"\u0000\u0000kj\u0001\u0000\u0000\u0000l\u001e\u0001\u0000\u0000\u0000"+
		"mn\u0005=\u0000\u0000no\u0005=\u0000\u0000o \u0001\u0000\u0000\u0000p"+
		"r\u0005#\u0000\u0000qs\b\u0001\u0000\u0000rq\u0001\u0000\u0000\u0000s"+
		"t\u0001\u0000\u0000\u0000tr\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000"+
		"\u0000uv\u0001\u0000\u0000\u0000vw\u0006\u0010\u0000\u0000w\"\u0001\u0000"+
		"\u0000\u0000xy\u0007\u0002\u0000\u0000y$\u0001\u0000\u0000\u0000z{\u0007"+
		"\u0003\u0000\u0000{&\u0001\u0000\u0000\u0000\b\u0000IKOT_kt\u0001\u0000"+
		"\u0001\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}