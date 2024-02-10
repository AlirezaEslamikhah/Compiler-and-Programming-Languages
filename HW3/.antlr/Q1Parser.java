// Generated from c://Users//lenovo//Desktop//Term7//Compiler//HW3//Q1.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class Q1Parser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, IF=7, WHILE=8, INT=9, 
		BOOL=10, ID=11, INTTYPE=12, BOOLTYPE=13, WS=14, RELOP=15, EQ=16, COMMENT=17;
	public static final int
		RULE_start = 0, RULE_ifst = 1, RULE_whilest = 2, RULE_statement = 3, RULE_compoundst = 4, 
		RULE_assignment = 5, RULE_condition = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "ifst", "whilest", "statement", "compoundst", "assignment", 
			"condition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "';'", "'if'", "'while'", "'int'", 
			"'boolean'", null, null, null, null, null, "'=='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, "IF", "WHILE", "INT", "BOOL", 
			"ID", "INTTYPE", "BOOLTYPE", "WS", "RELOP", "EQ", "COMMENT"
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

	@Override
	public String getGrammarFileName() { return "Q1.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public Q1Parser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(Q1Parser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public List<CompoundstContext> compoundst() {
			return getRuleContexts(CompoundstContext.class);
		}
		public CompoundstContext compoundst(int i) {
			return getRuleContext(CompoundstContext.class,i);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(18);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3976L) != 0)) {
				{
				setState(16);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
				case 1:
					{
					setState(14);
					statement();
					}
					break;
				case 2:
					{
					setState(15);
					compoundst();
					}
					break;
				}
				}
				setState(20);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(21);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode IF() { return getToken(Q1Parser.IF, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public IfstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterIfst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitIfst(this);
		}
	}

	public final IfstContext ifst() throws RecognitionException {
		IfstContext _localctx = new IfstContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_ifst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			match(IF);
			setState(24);
			match(T__0);
			setState(25);
			condition();
			setState(26);
			match(T__1);
			setState(27);
			match(T__2);
			setState(29); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(28);
				statement();
				}
				}
				setState(31); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 3976L) != 0) );
			setState(33);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhilestContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode WHILE() { return getToken(Q1Parser.WHILE, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public WhilestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilest; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterWhilest(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitWhilest(this);
		}
	}

	public final WhilestContext whilest() throws RecognitionException {
		WhilestContext _localctx = new WhilestContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_whilest);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(35);
			match(WHILE);
			setState(36);
			match(T__0);
			setState(37);
			condition();
			setState(38);
			match(T__1);
			setState(39);
			match(T__2);
			setState(43);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3976L) != 0)) {
				{
				{
				setState(40);
				statement();
				}
				}
				setState(45);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(46);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public IfstContext ifst() {
			return getRuleContext(IfstContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public WhilestContext whilest() {
			return getRuleContext(WhilestContext.class,0);
		}
		public CompoundstContext compoundst() {
			return getRuleContext(CompoundstContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(52);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case IF:
				enterOuterAlt(_localctx, 1);
				{
				setState(48);
				ifst();
				}
				break;
			case INT:
			case BOOL:
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(49);
				assignment();
				}
				break;
			case WHILE:
				enterOuterAlt(_localctx, 3);
				{
				setState(50);
				whilest();
				}
				break;
			case T__2:
				enterOuterAlt(_localctx, 4);
				{
				setState(51);
				compoundst();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompoundstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CompoundstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterCompoundst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitCompoundst(this);
		}
	}

	public final CompoundstContext compoundst() throws RecognitionException {
		CompoundstContext _localctx = new CompoundstContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_compoundst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			match(T__2);
			{
			setState(58);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 3976L) != 0)) {
				{
				{
				setState(55);
				statement();
				}
				}
				setState(60);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
			setState(61);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(Q1Parser.ID, 0); }
		public TerminalNode INTTYPE() { return getToken(Q1Parser.INTTYPE, 0); }
		public TerminalNode INT() { return getToken(Q1Parser.INT, 0); }
		public TerminalNode BOOLTYPE() { return getToken(Q1Parser.BOOLTYPE, 0); }
		public TerminalNode BOOL() { return getToken(Q1Parser.BOOL, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitAssignment(this);
		}
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assignment);
		int _la;
		try {
			setState(77);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(64);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==INT) {
					{
					setState(63);
					match(INT);
					}
				}

				setState(66);
				match(ID);
				setState(67);
				match(T__4);
				setState(68);
				match(INTTYPE);
				setState(69);
				match(T__5);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(71);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==BOOL) {
					{
					setState(70);
					match(BOOL);
					}
				}

				setState(73);
				match(ID);
				setState(74);
				match(T__4);
				setState(75);
				match(BOOLTYPE);
				setState(76);
				match(T__5);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode BOOLTYPE() { return getToken(Q1Parser.BOOLTYPE, 0); }
		public List<TerminalNode> ID() { return getTokens(Q1Parser.ID); }
		public TerminalNode ID(int i) {
			return getToken(Q1Parser.ID, i);
		}
		public TerminalNode RELOP() { return getToken(Q1Parser.RELOP, 0); }
		public TerminalNode INTTYPE() { return getToken(Q1Parser.INTTYPE, 0); }
		public TerminalNode EQ() { return getToken(Q1Parser.EQ, 0); }
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).enterCondition(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof Q1Listener ) ((Q1Listener)listener).exitCondition(this);
		}
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_condition);
		try {
			setState(89);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(79);
				match(BOOLTYPE);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(80);
				match(ID);
				setState(81);
				match(RELOP);
				setState(82);
				match(ID);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(83);
				match(ID);
				setState(84);
				match(RELOP);
				setState(85);
				match(INTTYPE);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(86);
				match(ID);
				setState(87);
				match(EQ);
				setState(88);
				match(BOOLTYPE);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0011\\\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0005"+
		"\u0000\u0011\b\u0000\n\u0000\f\u0000\u0014\t\u0000\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0004\u0001\u001e\b\u0001\u000b\u0001\f\u0001\u001f\u0001\u0001\u0001"+
		"\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0005\u0002*\b\u0002\n\u0002\f\u0002-\t\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u00035\b"+
		"\u0003\u0001\u0004\u0001\u0004\u0005\u00049\b\u0004\n\u0004\f\u0004<\t"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0003\u0005A\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005H\b"+
		"\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005N\b"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006Z\b"+
		"\u0006\u0001\u0006\u0000\u0000\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000"+
		"\u0000b\u0000\u0012\u0001\u0000\u0000\u0000\u0002\u0017\u0001\u0000\u0000"+
		"\u0000\u0004#\u0001\u0000\u0000\u0000\u00064\u0001\u0000\u0000\u0000\b"+
		"6\u0001\u0000\u0000\u0000\nM\u0001\u0000\u0000\u0000\fY\u0001\u0000\u0000"+
		"\u0000\u000e\u0011\u0003\u0006\u0003\u0000\u000f\u0011\u0003\b\u0004\u0000"+
		"\u0010\u000e\u0001\u0000\u0000\u0000\u0010\u000f\u0001\u0000\u0000\u0000"+
		"\u0011\u0014\u0001\u0000\u0000\u0000\u0012\u0010\u0001\u0000\u0000\u0000"+
		"\u0012\u0013\u0001\u0000\u0000\u0000\u0013\u0015\u0001\u0000\u0000\u0000"+
		"\u0014\u0012\u0001\u0000\u0000\u0000\u0015\u0016\u0005\u0000\u0000\u0001"+
		"\u0016\u0001\u0001\u0000\u0000\u0000\u0017\u0018\u0005\u0007\u0000\u0000"+
		"\u0018\u0019\u0005\u0001\u0000\u0000\u0019\u001a\u0003\f\u0006\u0000\u001a"+
		"\u001b\u0005\u0002\u0000\u0000\u001b\u001d\u0005\u0003\u0000\u0000\u001c"+
		"\u001e\u0003\u0006\u0003\u0000\u001d\u001c\u0001\u0000\u0000\u0000\u001e"+
		"\u001f\u0001\u0000\u0000\u0000\u001f\u001d\u0001\u0000\u0000\u0000\u001f"+
		" \u0001\u0000\u0000\u0000 !\u0001\u0000\u0000\u0000!\"\u0005\u0004\u0000"+
		"\u0000\"\u0003\u0001\u0000\u0000\u0000#$\u0005\b\u0000\u0000$%\u0005\u0001"+
		"\u0000\u0000%&\u0003\f\u0006\u0000&\'\u0005\u0002\u0000\u0000\'+\u0005"+
		"\u0003\u0000\u0000(*\u0003\u0006\u0003\u0000)(\u0001\u0000\u0000\u0000"+
		"*-\u0001\u0000\u0000\u0000+)\u0001\u0000\u0000\u0000+,\u0001\u0000\u0000"+
		"\u0000,.\u0001\u0000\u0000\u0000-+\u0001\u0000\u0000\u0000./\u0005\u0004"+
		"\u0000\u0000/\u0005\u0001\u0000\u0000\u000005\u0003\u0002\u0001\u0000"+
		"15\u0003\n\u0005\u000025\u0003\u0004\u0002\u000035\u0003\b\u0004\u0000"+
		"40\u0001\u0000\u0000\u000041\u0001\u0000\u0000\u000042\u0001\u0000\u0000"+
		"\u000043\u0001\u0000\u0000\u00005\u0007\u0001\u0000\u0000\u00006:\u0005"+
		"\u0003\u0000\u000079\u0003\u0006\u0003\u000087\u0001\u0000\u0000\u0000"+
		"9<\u0001\u0000\u0000\u0000:8\u0001\u0000\u0000\u0000:;\u0001\u0000\u0000"+
		"\u0000;=\u0001\u0000\u0000\u0000<:\u0001\u0000\u0000\u0000=>\u0005\u0004"+
		"\u0000\u0000>\t\u0001\u0000\u0000\u0000?A\u0005\t\u0000\u0000@?\u0001"+
		"\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AB\u0001\u0000\u0000\u0000"+
		"BC\u0005\u000b\u0000\u0000CD\u0005\u0005\u0000\u0000DE\u0005\f\u0000\u0000"+
		"EN\u0005\u0006\u0000\u0000FH\u0005\n\u0000\u0000GF\u0001\u0000\u0000\u0000"+
		"GH\u0001\u0000\u0000\u0000HI\u0001\u0000\u0000\u0000IJ\u0005\u000b\u0000"+
		"\u0000JK\u0005\u0005\u0000\u0000KL\u0005\r\u0000\u0000LN\u0005\u0006\u0000"+
		"\u0000M@\u0001\u0000\u0000\u0000MG\u0001\u0000\u0000\u0000N\u000b\u0001"+
		"\u0000\u0000\u0000OZ\u0005\r\u0000\u0000PQ\u0005\u000b\u0000\u0000QR\u0005"+
		"\u000f\u0000\u0000RZ\u0005\u000b\u0000\u0000ST\u0005\u000b\u0000\u0000"+
		"TU\u0005\u000f\u0000\u0000UZ\u0005\f\u0000\u0000VW\u0005\u000b\u0000\u0000"+
		"WX\u0005\u0010\u0000\u0000XZ\u0005\r\u0000\u0000YO\u0001\u0000\u0000\u0000"+
		"YP\u0001\u0000\u0000\u0000YS\u0001\u0000\u0000\u0000YV\u0001\u0000\u0000"+
		"\u0000Z\r\u0001\u0000\u0000\u0000\n\u0010\u0012\u001f+4:@GMY";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}