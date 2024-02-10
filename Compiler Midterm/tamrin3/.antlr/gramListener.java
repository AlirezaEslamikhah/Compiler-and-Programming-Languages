// Generated from c://Users//lenovo//Desktop//Compiler Midterm//tamrin3//gram.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramParser}.
 */
public interface gramListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(gramParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(gramParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#ifst}.
	 * @param ctx the parse tree
	 */
	void enterIfst(gramParser.IfstContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#ifst}.
	 * @param ctx the parse tree
	 */
	void exitIfst(gramParser.IfstContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#whilest}.
	 * @param ctx the parse tree
	 */
	void enterWhilest(gramParser.WhilestContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#whilest}.
	 * @param ctx the parse tree
	 */
	void exitWhilest(gramParser.WhilestContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(gramParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(gramParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#compoundst}.
	 * @param ctx the parse tree
	 */
	void enterCompoundst(gramParser.CompoundstContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#compoundst}.
	 * @param ctx the parse tree
	 */
	void exitCompoundst(gramParser.CompoundstContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#define}.
	 * @param ctx the parse tree
	 */
	void enterDefine(gramParser.DefineContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#define}.
	 * @param ctx the parse tree
	 */
	void exitDefine(gramParser.DefineContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(gramParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(gramParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramParser#cond}.
	 * @param ctx the parse tree
	 */
	void enterCond(gramParser.CondContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramParser#cond}.
	 * @param ctx the parse tree
	 */
	void exitCond(gramParser.CondContext ctx);
}