// Generated from c://Users//lenovo//Desktop//Term7//Compiler//HW3//Q1.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link Q1Parser}.
 */
public interface Q1Listener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link Q1Parser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(Q1Parser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(Q1Parser.StartContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#ifst}.
	 * @param ctx the parse tree
	 */
	void enterIfst(Q1Parser.IfstContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#ifst}.
	 * @param ctx the parse tree
	 */
	void exitIfst(Q1Parser.IfstContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#whilest}.
	 * @param ctx the parse tree
	 */
	void enterWhilest(Q1Parser.WhilestContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#whilest}.
	 * @param ctx the parse tree
	 */
	void exitWhilest(Q1Parser.WhilestContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(Q1Parser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(Q1Parser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#compoundst}.
	 * @param ctx the parse tree
	 */
	void enterCompoundst(Q1Parser.CompoundstContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#compoundst}.
	 * @param ctx the parse tree
	 */
	void exitCompoundst(Q1Parser.CompoundstContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(Q1Parser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(Q1Parser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link Q1Parser#condition}.
	 * @param ctx the parse tree
	 */
	void enterCondition(Q1Parser.ConditionContext ctx);
	/**
	 * Exit a parse tree produced by {@link Q1Parser#condition}.
	 * @param ctx the parse tree
	 */
	void exitCondition(Q1Parser.ConditionContext ctx);
}