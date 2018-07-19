<%@ page contentType="text/html;charset=utf-8"%>
<head>
    <jsp:include page="head.jsp"/>
</head>
<html>
    <body bgcolor=yellow>
        <P><font size=5 color=red>This is error.jsp</font>
        <font size=2>
            <% String s=request.getParameter("mess");
            out.println("<br>传递过来的错误信息"+s);
            %>
            <br><img src ="error.jpg" width="180" height="220"></img>
        </font>
    </body>
</html> 
