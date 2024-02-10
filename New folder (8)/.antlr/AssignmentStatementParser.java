// Generated from c://Users//lenovo//Desktop//New folder (8)//AssignmentStatement.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class AssignmentStatementParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		INT=18, FLOAT=19, String=20, ID=21, ARRAY_TYPE=22, INT_ARRAY=23, FLOAT_ARRAY=24, 
		STRING_ARRAY=25, WS=26, NEWLINE=27, RELOP=28;
	public static final int
		RULE_start = 0, RULE_prog = 1, RULE_statement = 2, RULE_ifst = 3, RULE_cond = 4, 
		RULE_assign = 5, RULE_compoundst = 6, RULE_forst = 7, RULE_whilest = 8, 
		RULE_expr = 9, RULE_term = 10, RULE_factor = 11, RULE_number = 12, RULE_array = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "prog", "statement", "ifst", "cond", "assign", "compoundst", 
			"forst", "whilest", "expr", "term", "factor", "number", "array"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'then'", "'else'", "'>'", "':='", "'begin'", "'end'", 
			"'for'", "'to'", "'do'", "'while'", "'+'", "'-'", "'*'", "'/'", "'('", 
			"')'", null, null, null, null, null, null, null, null, null, "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "INT", "FLOAT", "String", "ID", "ARRAY_TYPE", 
			"INT_ARRAY", "FLOAT_ARRAY", "STRING_ARRAY", "WS", "NEWLINE", "RELOP"
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
	public String getGrammarFileName() { return "AssignmentStatement.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AssignmentStatementParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ProgContext prog() {
			return getRuleContext(ProgContext.class,0);
		}
		public TerminalNode EOF() { return getToken(AssignmentStatementParser.EOF, 0); }
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			prog();
			setState(29);
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
	public static class ProgContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public CompoundstContext compoundst() {
			return getRuleContext(CompoundstContext.class,0);
		}
		public TerminalNode NEWLINE() { return getToken(AssignmentStatementParser.NEWLINE, 0); }
		public TerminalNode EOF() { return getToken(AssignmentStatementParser.EOF, 0); }
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterProg(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitProg(this);
		}
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_prog);
		int _la;
		try {
			setState(37);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,0,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(31);
				compoundst();
				setState(32);
				_la = _input.LA(1);
				if ( !(_la==EOF || _la==NEWLINE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(34);
				statement();
				setState(35);
				_la = _input.LA(1);
				if ( !(_la==EOF || _la==NEWLINE) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
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
	public static class StatementContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public IfstContext ifst() {
			return getRuleContext(IfstContext.class,0);
		}
		public AssignContext assign() {
			return getRuleContext(AssignContext.class,0);
		}
		public CompoundstContext compoundst() {
			return getRuleContext(CompoundstContext.class,0);
		}
		public ForstContext forst() {
			return getRuleContext(ForstContext.class,0);
		}
		public WhilestContext whilest() {
			return getRuleContext(WhilestContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterStatement(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitStatement(this);
		}
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_statement);
		try {
			setState(44);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__0:
				enterOuterAlt(_localctx, 1);
				{
				setState(39);
				ifst();
				}
				break;
			case ID:
				enterOuterAlt(_localctx, 2);
				{
				setState(40);
				assign();
				}
				break;
			case T__5:
				enterOuterAlt(_localctx, 3);
				{
				setState(41);
				compoundst();
				}
				break;
			case T__7:
				enterOuterAlt(_localctx, 4);
				{
				setState(42);
				forst();
				}
				break;
			case T__10:
				enterOuterAlt(_localctx, 5);
				{
				setState(43);
				whilest();
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
	public static class IfstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
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
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterIfst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitIfst(this);
		}
	}

	public final IfstContext ifst() throws RecognitionException {
		IfstContext _localctx = new IfstContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_ifst);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(46);
			match(T__0);
			setState(47);
			cond();
			setState(48);
			match(T__1);
			setState(49);
			statement();
			setState(52);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,2,_ctx) ) {
			case 1:
				{
				setState(50);
				match(T__2);
				setState(51);
				statement();
				}
				break;
			}
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
	public static class CondContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CondContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_cond; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCond(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCond(this);
		}
	}

	public final CondContext cond() throws RecognitionException {
		CondContext _localctx = new CondContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_cond);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(54);
			expr(0);
			setState(55);
			match(T__3);
			setState(56);
			expr(0);
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
	public static class AssignContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assign; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterAssign(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitAssign(this);
		}
	}

	public final AssignContext assign() throws RecognitionException {
		AssignContext _localctx = new AssignContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_assign);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(ID);
			setState(59);
			match(T__4);
			setState(60);
			expr(0);
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
		public List<TerminalNode> NEWLINE() { return getTokens(AssignmentStatementParser.NEWLINE); }
		public TerminalNode NEWLINE(int i) {
			return getToken(AssignmentStatementParser.NEWLINE, i);
		}
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
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterCompoundst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitCompoundst(this);
		}
	}

	public final CompoundstContext compoundst() throws RecognitionException {
		CompoundstContext _localctx = new CompoundstContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_compoundst);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(62);
			match(T__5);
			setState(63);
			match(NEWLINE);
			setState(67); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(64);
				statement();
				setState(65);
				match(NEWLINE);
				}
				}
				setState(69); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 2099522L) != 0) );
			setState(71);
			match(T__6);
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
	public static class ForstContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ForstContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forst; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterForst(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitForst(this);
		}
	}

	public final ForstContext forst() throws RecognitionException {
		ForstContext _localctx = new ForstContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_forst);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(T__7);
			setState(74);
			match(ID);
			setState(75);
			match(T__4);
			setState(76);
			expr(0);
			setState(77);
			match(T__8);
			setState(78);
			expr(0);
			setState(79);
			match(T__9);
			setState(80);
			statement();
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
		public CondContext cond() {
			return getRuleContext(CondContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhilestContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whilest; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterWhilest(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitWhilest(this);
		}
	}

	public final WhilestContext whilest() throws RecognitionException {
		WhilestContext _localctx = new WhilestContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whilest);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(T__10);
			setState(83);
			cond();
			setState(84);
			match(T__9);
			setState(85);
			statement();
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
	public static class ExprContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_minusContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_minusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_minus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_minus(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_plusContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_plusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_plus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_plus(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term4Context extends ExprContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Term4Context(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm4(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm4(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Expr_term_relopContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public TerminalNode RELOP() { return getToken(AssignmentStatementParser.RELOP, 0); }
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public Expr_term_relopContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterExpr_term_relop(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitExpr_term_relop(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 18;
		enterRecursionRule(_localctx, 18, RULE_expr, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Term4Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(88);
			term(0);
			}
			_ctx.stop = _input.LT(-1);
			setState(101);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(99);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,4,_ctx) ) {
					case 1:
						{
						_localctx = new Expr_term_plusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(90);
						if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
						setState(91);
						match(T__11);
						setState(92);
						term(0);
						}
						break;
					case 2:
						{
						_localctx = new Expr_term_minusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(93);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(94);
						match(T__12);
						setState(95);
						term(0);
						}
						break;
					case 3:
						{
						_localctx = new Expr_term_relopContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(96);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(97);
						match(RELOP);
						setState(98);
						term(0);
						}
						break;
					}
					} 
				}
				setState(103);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,5,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TermContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public TermContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_term; }
	 
		public TermContext() { }
		public void copyFrom(TermContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term_fact_divideContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_fact_divideContext(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm_fact_divide(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm_fact_divide(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Term_fact_mutiplyContext extends TermContext {
		public TermContext term() {
			return getRuleContext(TermContext.class,0);
		}
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Term_fact_mutiplyContext(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterTerm_fact_mutiply(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitTerm_fact_mutiply(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Factor3Context extends TermContext {
		public FactorContext factor() {
			return getRuleContext(FactorContext.class,0);
		}
		public Factor3Context(TermContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFactor3(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFactor3(this);
		}
	}

	public final TermContext term() throws RecognitionException {
		return term(0);
	}

	private TermContext term(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		TermContext _localctx = new TermContext(_ctx, _parentState);
		TermContext _prevctx = _localctx;
		int _startState = 20;
		enterRecursionRule(_localctx, 20, RULE_term, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			{
			_localctx = new Factor3Context(_localctx);
			_ctx = _localctx;
			_prevctx = _localctx;

			setState(105);
			factor();
			}
			_ctx.stop = _input.LT(-1);
			setState(115);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(113);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
					case 1:
						{
						_localctx = new Term_fact_mutiplyContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(107);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(108);
						match(T__13);
						setState(109);
						factor();
						}
						break;
					case 2:
						{
						_localctx = new Term_fact_divideContext(new TermContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_term);
						setState(110);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(111);
						match(T__14);
						setState(112);
						factor();
						}
						break;
					}
					} 
				}
				setState(117);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FactorContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public FactorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_factor; }
	 
		public FactorContext() { }
		public void copyFrom(FactorContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_exprContext extends FactorContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public Fact_exprContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_expr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_expr(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_idContext extends FactorContext {
		public TerminalNode ID() { return getToken(AssignmentStatementParser.ID, 0); }
		public Fact_idContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_id(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_id(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_numberContext extends FactorContext {
		public NumberContext number() {
			return getRuleContext(NumberContext.class,0);
		}
		public Fact_numberContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_number(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_number(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Fact_arrayContext extends FactorContext {
		public ArrayContext array() {
			return getRuleContext(ArrayContext.class,0);
		}
		public Fact_arrayContext(FactorContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterFact_array(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitFact_array(this);
		}
	}

	public final FactorContext factor() throws RecognitionException {
		FactorContext _localctx = new FactorContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_factor);
		try {
			setState(125);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__15:
				_localctx = new Fact_exprContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(118);
				match(T__15);
				setState(119);
				expr(0);
				setState(120);
				match(T__16);
				}
				break;
			case ID:
				_localctx = new Fact_idContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(122);
				match(ID);
				}
				break;
			case INT:
			case FLOAT:
				_localctx = new Fact_numberContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(123);
				number();
				}
				break;
			case INT_ARRAY:
			case FLOAT_ARRAY:
			case STRING_ARRAY:
				_localctx = new Fact_arrayContext(_localctx);
				enterOuterAlt(_localctx, 4);
				{
				setState(124);
				array();
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
	public static class NumberContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public NumberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_number; }
	 
		public NumberContext() { }
		public void copyFrom(NumberContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Number_floatContext extends NumberContext {
		public TerminalNode FLOAT() { return getToken(AssignmentStatementParser.FLOAT, 0); }
		public Number_floatContext(NumberContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterNumber_float(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitNumber_float(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Number_intContext extends NumberContext {
		public TerminalNode INT() { return getToken(AssignmentStatementParser.INT, 0); }
		public Number_intContext(NumberContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterNumber_int(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitNumber_int(this);
		}
	}

	public final NumberContext number() throws RecognitionException {
		NumberContext _localctx = new NumberContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_number);
		try {
			setState(129);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case FLOAT:
				_localctx = new Number_floatContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(127);
				match(FLOAT);
				}
				break;
			case INT:
				_localctx = new Number_intContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(128);
				match(INT);
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
	public static class ArrayContext extends ParserRuleContext {
		public  value_attr = str();
		public  type_attr = str();
		public ArrayContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_array; }
	 
		public ArrayContext() { }
		public void copyFrom(ArrayContext ctx) {
			super.copyFrom(ctx);
			this.value_attr = ctx.value_attr;
			this.type_attr = ctx.type_attr;
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_floatContext extends ArrayContext {
		public TerminalNode FLOAT_ARRAY() { return getToken(AssignmentStatementParser.FLOAT_ARRAY, 0); }
		public Array_floatContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_float(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_float(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_stringContext extends ArrayContext {
		public TerminalNode STRING_ARRAY() { return getToken(AssignmentStatementParser.STRING_ARRAY, 0); }
		public Array_stringContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_string(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_string(this);
		}
	}
	@SuppressWarnings("CheckReturnValue")
	public static class Array_intContext extends ArrayContext {
		public TerminalNode INT_ARRAY() { return getToken(AssignmentStatementParser.INT_ARRAY, 0); }
		public Array_intContext(ArrayContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).enterArray_int(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof AssignmentStatementListener ) ((AssignmentStatementListener)listener).exitArray_int(this);
		}
	}

	public final ArrayContext array() throws RecognitionException {
		ArrayContext _localctx = new ArrayContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_array);
		try {
			setState(134);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT_ARRAY:
				_localctx = new Array_intContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(131);
				match(INT_ARRAY);
				}
				break;
			case FLOAT_ARRAY:
				_localctx = new Array_floatContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(132);
				match(FLOAT_ARRAY);
				}
				break;
			case STRING_ARRAY:
				_localctx = new Array_stringContext(_localctx);
				enterOuterAlt(_localctx, 3);
				{
				setState(133);
				match(STRING_ARRAY);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 9:
			return expr_sempred((ExprContext)_localctx, predIndex);
		case 10:
			return term_sempred((TermContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		case 1:
			return precpred(_ctx, 3);
		case 2:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean term_sempred(TermContext _localctx, int predIndex) {
		switch (predIndex) {
		case 3:
			return precpred(_ctx, 3);
		case 4:
			return precpred(_ctx, 2);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u001c\u0089\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003"+
		"\u0001&\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0003\u0002-\b\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u00035\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0004"+
		"\u0006D\b\u0006\u000b\u0006\f\u0006E\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0005\td\b\t\n\t\f\tg\t\t\u0001\n\u0001\n\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0005\nr\b\n\n\n\f\nu\t\n\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0003\u000b~\b\u000b\u0001\f\u0001\f\u0003\f\u0082\b\f\u0001\r"+
		"\u0001\r\u0001\r\u0003\r\u0087\b\r\u0001\r\u0000\u0002\u0012\u0014\u000e"+
		"\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a"+
		"\u0000\u0001\u0001\u0001\u001b\u001b\u008c\u0000\u001c\u0001\u0000\u0000"+
		"\u0000\u0002%\u0001\u0000\u0000\u0000\u0004,\u0001\u0000\u0000\u0000\u0006"+
		".\u0001\u0000\u0000\u0000\b6\u0001\u0000\u0000\u0000\n:\u0001\u0000\u0000"+
		"\u0000\f>\u0001\u0000\u0000\u0000\u000eI\u0001\u0000\u0000\u0000\u0010"+
		"R\u0001\u0000\u0000\u0000\u0012W\u0001\u0000\u0000\u0000\u0014h\u0001"+
		"\u0000\u0000\u0000\u0016}\u0001\u0000\u0000\u0000\u0018\u0081\u0001\u0000"+
		"\u0000\u0000\u001a\u0086\u0001\u0000\u0000\u0000\u001c\u001d\u0003\u0002"+
		"\u0001\u0000\u001d\u001e\u0005\u0000\u0000\u0001\u001e\u0001\u0001\u0000"+
		"\u0000\u0000\u001f \u0003\f\u0006\u0000 !\u0007\u0000\u0000\u0000!&\u0001"+
		"\u0000\u0000\u0000\"#\u0003\u0004\u0002\u0000#$\u0007\u0000\u0000\u0000"+
		"$&\u0001\u0000\u0000\u0000%\u001f\u0001\u0000\u0000\u0000%\"\u0001\u0000"+
		"\u0000\u0000&\u0003\u0001\u0000\u0000\u0000\'-\u0003\u0006\u0003\u0000"+
		"(-\u0003\n\u0005\u0000)-\u0003\f\u0006\u0000*-\u0003\u000e\u0007\u0000"+
		"+-\u0003\u0010\b\u0000,\'\u0001\u0000\u0000\u0000,(\u0001\u0000\u0000"+
		"\u0000,)\u0001\u0000\u0000\u0000,*\u0001\u0000\u0000\u0000,+\u0001\u0000"+
		"\u0000\u0000-\u0005\u0001\u0000\u0000\u0000./\u0005\u0001\u0000\u0000"+
		"/0\u0003\b\u0004\u000001\u0005\u0002\u0000\u000014\u0003\u0004\u0002\u0000"+
		"23\u0005\u0003\u0000\u000035\u0003\u0004\u0002\u000042\u0001\u0000\u0000"+
		"\u000045\u0001\u0000\u0000\u00005\u0007\u0001\u0000\u0000\u000067\u0003"+
		"\u0012\t\u000078\u0005\u0004\u0000\u000089\u0003\u0012\t\u00009\t\u0001"+
		"\u0000\u0000\u0000:;\u0005\u0015\u0000\u0000;<\u0005\u0005\u0000\u0000"+
		"<=\u0003\u0012\t\u0000=\u000b\u0001\u0000\u0000\u0000>?\u0005\u0006\u0000"+
		"\u0000?C\u0005\u001b\u0000\u0000@A\u0003\u0004\u0002\u0000AB\u0005\u001b"+
		"\u0000\u0000BD\u0001\u0000\u0000\u0000C@\u0001\u0000\u0000\u0000DE\u0001"+
		"\u0000\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000"+
		"FG\u0001\u0000\u0000\u0000GH\u0005\u0007\u0000\u0000H\r\u0001\u0000\u0000"+
		"\u0000IJ\u0005\b\u0000\u0000JK\u0005\u0015\u0000\u0000KL\u0005\u0005\u0000"+
		"\u0000LM\u0003\u0012\t\u0000MN\u0005\t\u0000\u0000NO\u0003\u0012\t\u0000"+
		"OP\u0005\n\u0000\u0000PQ\u0003\u0004\u0002\u0000Q\u000f\u0001\u0000\u0000"+
		"\u0000RS\u0005\u000b\u0000\u0000ST\u0003\b\u0004\u0000TU\u0005\n\u0000"+
		"\u0000UV\u0003\u0004\u0002\u0000V\u0011\u0001\u0000\u0000\u0000WX\u0006"+
		"\t\uffff\uffff\u0000XY\u0003\u0014\n\u0000Ye\u0001\u0000\u0000\u0000Z"+
		"[\n\u0004\u0000\u0000[\\\u0005\f\u0000\u0000\\d\u0003\u0014\n\u0000]^"+
		"\n\u0003\u0000\u0000^_\u0005\r\u0000\u0000_d\u0003\u0014\n\u0000`a\n\u0002"+
		"\u0000\u0000ab\u0005\u001c\u0000\u0000bd\u0003\u0014\n\u0000cZ\u0001\u0000"+
		"\u0000\u0000c]\u0001\u0000\u0000\u0000c`\u0001\u0000\u0000\u0000dg\u0001"+
		"\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000\u0000"+
		"f\u0013\u0001\u0000\u0000\u0000ge\u0001\u0000\u0000\u0000hi\u0006\n\uffff"+
		"\uffff\u0000ij\u0003\u0016\u000b\u0000js\u0001\u0000\u0000\u0000kl\n\u0003"+
		"\u0000\u0000lm\u0005\u000e\u0000\u0000mr\u0003\u0016\u000b\u0000no\n\u0002"+
		"\u0000\u0000op\u0005\u000f\u0000\u0000pr\u0003\u0016\u000b\u0000qk\u0001"+
		"\u0000\u0000\u0000qn\u0001\u0000\u0000\u0000ru\u0001\u0000\u0000\u0000"+
		"sq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000t\u0015\u0001\u0000"+
		"\u0000\u0000us\u0001\u0000\u0000\u0000vw\u0005\u0010\u0000\u0000wx\u0003"+
		"\u0012\t\u0000xy\u0005\u0011\u0000\u0000y~\u0001\u0000\u0000\u0000z~\u0005"+
		"\u0015\u0000\u0000{~\u0003\u0018\f\u0000|~\u0003\u001a\r\u0000}v\u0001"+
		"\u0000\u0000\u0000}z\u0001\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000"+
		"}|\u0001\u0000\u0000\u0000~\u0017\u0001\u0000\u0000\u0000\u007f\u0082"+
		"\u0005\u0013\u0000\u0000\u0080\u0082\u0005\u0012\u0000\u0000\u0081\u007f"+
		"\u0001\u0000\u0000\u0000\u0081\u0080\u0001\u0000\u0000\u0000\u0082\u0019"+
		"\u0001\u0000\u0000\u0000\u0083\u0087\u0005\u0017\u0000\u0000\u0084\u0087"+
		"\u0005\u0018\u0000\u0000\u0085\u0087\u0005\u0019\u0000\u0000\u0086\u0083"+
		"\u0001\u0000\u0000\u0000\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0085"+
		"\u0001\u0000\u0000\u0000\u0087\u001b\u0001\u0000\u0000\u0000\u000b%,4"+
		"Eceqs}\u0081\u0086";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}